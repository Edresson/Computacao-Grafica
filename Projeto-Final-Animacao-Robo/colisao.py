#!/usr/bin/env python
# coding: utf8
'''
funcão de detectação de colisão pygame 
tutorial em: http://www.youtube.com/watch?v=TJs0l0lj7dk&list=PL0AB023E769342AFE&index=34
'''
import sys, pygame 
from pygame.locals import * 
from pygame.constants import * 
from cinematica_inversa import Poligono 

class game_screen():
    def __init__(self, width=800, height=600):
        self.viewport = (width,height)
        self.width = width
        self.height = height
        self.srf = pygame.display.set_mode(self.viewport, OPENGL | DOUBLEBUF )#FULLSCREEN | HWSURFACE )


def distancia_entre_pontos(c1,c2):
    
    distancia_entre_pontos.Pvec .x = c2.x-c1.x
    distancia_entre_pontos.Pvec .y= c2.y-c1.y
    distancia_entre_pontos.Pvec .z = c2.z-c1.z
    return (distancia_entre_pontos.Pvec.x*distancia_entre_pontos.Pvec.x + distancia_entre_pontos.Pvec.y *
            distancia_entre_pontos.Pvec.y +distancia_entre_pontos.Pvec.z*distancia_entre_pontos.Pvec.z)
distancia_entre_pontos.Pvec = Poligono(0,0,0)

def colisao_bola(c1,r1,c2,r2,):
    distancia=distancia_entre_pontos(c1,c2)
    if(distancia<=(r1+r2)*(r1+r2)): #logica para esfera simples retirada do video
        return True
    else:
        return False
