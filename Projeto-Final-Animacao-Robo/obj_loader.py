#!/usr/bin/env python
# coding: utf8
'''Retirado de  um tutorial disponivel  no site da pygame, exemplo pygame obj loader'''
import pygame
from OpenGL.GL import *
import sys

PATH = 'Modelos/'

#load the filename textures (only BMP, R5G6B5 format)
def loadTexture(filename):   
    img = pygame.image.load(PATH+filename)
    pixels = pygame.image.tostring(img, 'RGBA', 1)
    img_id = glGenTextures(1)
    w, h = img.get_rect().size
    glBindTexture(GL_TEXTURE_2D, img_id)
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    #glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
    #glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, w, h, 0, GL_RGBA,
                GL_UNSIGNED_BYTE,  pixels)
    return img_id;


 
def MTL(filename):
    contents = {}
    mtl = None
    for line in open(PATH+filename, "r"):
        if line.startswith('#'): continue
        values = line.split()
        if not values: continue
        if values[0] == 'newmtl':
            mtl = contents[values[1]] = {}
        elif mtl is None:
            pass
            # ValueError, "mtl file doesn't start with newmtl stmt"
        elif values[0] == 'map_Kd':
            # load the texture referred to by this declaration
            mtl[values[0]] = values[1]
            surf = pygame.image.load(PATH+mtl['map_Kd'])
            image = pygame.image.tostring(surf, 'RGBA', 1)
            ix, iy = surf.get_rect().size
            texid = mtl['texture_Kd'] = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, texid)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER,
                GL_LINEAR)
            if mtl['map_Kd'] == "graph.bmp":
                #print 'making mipmaps of graph'
                glTexParameteri(GL_TEXTURE_2D, GL_GENERATE_MIPMAP,GL_TRUE)
            else:
                glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                                GL_LINEAR)
            #glGenerateMipmap(GL_TEXTURE_2D)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, ix, iy, 0, GL_RGBA,
                GL_UNSIGNED_BYTE, image)
        else:
            mtl[values[0]] = map(float, values[1:])#list of all of the materials in file
    return contents
 
class OBJ:
    def __init__(self, filename, swapyz=False, my_texture = False, use_mat = False):
        """Loads a Wavefront OBJ file. """
        self.vertices = []
        self.normals = []
        self.texcoords = []
        self.faces = []
        
        material = None
        for line in open(filename, "r"):
            if line.startswith('#'): continue
            values = line.split()
            if not values: continue
            if values[0] == 'v':
                v = map(float, values[1:4])
                if swapyz:
                    v = v[0], v[2], v[1]
                self.vertices.append(v)
            elif values[0] == 'vn':
                v = map(float, values[1:4])
                if swapyz:
                    v = v[0], v[2], v[1]
                self.normals.append(v)
            elif values[0] == 'vt':
                self.texcoords.append(map(float, values[1:3]))
            elif values[0] in ('usemtl', 'usemat'):
                material = values[1]
            elif values[0] == 'mtllib':
                self.mtl = MTL(values[1])
            elif values[0] == 'f':
                face = []
                texcoords = []
                norms = []
                for v in values[1:]:
                    w = v.split('/')
                    face.append(int(w[0]))
                    if len(w) >= 2 and len(w[1]) > 0:
                        texcoords.append(int(w[1]))
                    else:
                        texcoords.append(0)
                    if len(w) >= 3 and len(w[2]) > 0:
                        norms.append(int(w[2]))
                    else:
                        norms.append(0)
                self.faces.append((face, norms, texcoords, material))
 
        self.gl_list = glGenLists(1)
        glNewList(self.gl_list, GL_COMPILE)
        glEnable(GL_TEXTURE_2D)
        glFrontFace(GL_CCW)
        for face in (self.faces):
            vertices, normals, texture_coords, material = face
            mtl = self.mtl[material]
            if 'texture_Kd' in mtl:
                # use diffuse texmap
                glBindTexture(GL_TEXTURE_2D, mtl['texture_Kd'])
            else:
                if use_mat is not False:
                    glColor(*mtl['Kd']) 
                '''
                glDisable(GL_TEXTURE_2D) 
                glColor(*mtl['Kd']) 
                
                #call these variables in a class that pushes and pops atributes  
                if my_texture != False:           
                    #glDisable(GL_TEXTURE_2D)                
                    glColorMaterial(GL_FRONT, GL_DIFFUSE)
                    glColor(*mtl['Kd']) 
                glColorMaterial(GL_FRONT, GL_AMBIENT)
                glColor(mtl['Ka'])
                #tested this shininess works
                if all(i <= 128 for i in mtl['Ns']):
                    glMaterial(GL_FRONT, GL_SHININESS, mtl['Ns'] )
                else :
                    #print "shininess out of limits set to 128"
                    glMaterial(GL_FRONT, GL_SHININESS, 128 )
                #end of shininess
                glColorMaterial(GL_FRONT, GL_SPECULAR)
                glColor(mtl['Ks'])
                '''
            tex_pos = list()
            if len(vertices) == 3:
                self.texcoords = ([0,0], [.5,1], [1,0])
                ##print "triangle"
            if len(vertices) == 4:
                ##print "Quad"
                tex_pos = ([0,0], [1,0], [1,1], [0,1])

            glBegin(GL_POLYGON)
            for i in range(len(vertices)):
                if normals[i] > 0:
                    print(self.normals[normals[i] - 1])
                    glNormal3fv(self.normals[normals[i] - 1])
                if texture_coords[i] > 0:
                    ##print "found texture"
                    glTexCoord2fv(self.texcoords[texture_coords[i] - 1])
                
                if my_texture is not False:
                    glTexCoord2f(*tex_pos[i])
                    ##print "texture coordinates", tex_pos[i]
                
                glVertex3fv(self.vertices[vertices[i] - 1])
                
            glEnd()
        glDisable(GL_TEXTURE_2D)
        glEndList()
