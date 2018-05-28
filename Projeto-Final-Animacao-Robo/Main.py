#!/usr/bin/env python
# coding: utf8
import sys, pygame 
from pygame.locals import * 
from pygame.constants import * 
from OpenGL.GL import * 
from OpenGL.GLU import *
import random


from obj_loader import * #Objeto loader, usando pygame e pyopengl, baixado no site do pygame e adaptado ao projeto
from camera import *  # controle da camera e movimentação 


from colisao import * 
from cinematica_inversa import * 

pygame.init()

game = game_screen(1200,900) 


cine_inv = cordenadas() 
nova_angulos = plot_angulos(np.array([0.0]*5,dtype=float), 
                         np.array([0.0]*5,dtype=float))

bola_presa_cordenada = Poligono(68, -25, 181)

Braco_coord = Cordenadas_bracoMec([258.762, 141, 51.43, 0, 512])#Cordenadas iniciais

angulo = np.array([0.0]*5)
angulos_pinca = np.sort(np.arange(-90, 90, 5, dtype=int))
enter_apertado = 0 # 
contador = 0  

#localizacao da bola 
circ2 = Poligono(x=100.0, y=50.0, z=131.75)
r2 = 10 #raio distancia da bola

#usado para armazenar a cordenada da caixa para colocar a bola e relançar 
cordenada_caixa = Poligono(-2.0, -250.0, 30 )
caixa_raio_distancia = 25 #raio de distancia para o tamanho da caixa até que ponto aceitar

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


def init():#quarto_F_B_B, quarto_L_R_B, quarto_FB_T, quarto_LR_T,quarto_sill
    global bola, cubo, clock, base, ombro, bicep,quarto_T_B,texturabraco,caixinha, bicep001, pulso, suport_pinca, pinca, pinca001
    glClearColor(0.0, 0.0, 0.6, 0.0) #preto
    #glTranslatef(-10, 25, -130)
    
    #luz sobre  o braço mec
    diffuseLight = (0.7,0.7,0.7,1.0)#( 0.5, 0.5, 0.5, 1.0);#cor
    ambientLight= (0.2,0.2,0.2,1.0)#( 0.5, 0.5, 0.5, 0.7);#
    #emissiveLight = (1.0, 1.0, 1.0, 1.0);
    luzEspecular = (1.0, 1.0, 1.0, 1.0)
    lightPos = (-10, 400, -160.0, 0.0 );
    #mat_spec = (0.8, 0.2, 0.2, 1.0);
    #mat_diff = ( 0.8, 0.2, 0.2, 1.0);
    #mat_shin = (10.0);
    

    glLightfv(GL_LIGHT0, GL_AMBIENT, ambientLight);
    glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuseLight);
    glMaterialfv(GL_FRONT, GL_SPECULAR, luzEspecular);
    glLightfv(GL_LIGHT0, GL_POSITION, lightPos);
    #glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diff );
    #glMaterialfv(GL_FRONT, GL_SHININESS, mat_shin);
    

    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING)
    
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST);
    #luz em cima do quarto
   
    
    
    
    #glEnable(GL_DEPTH_TEST)
    
    # Habilita o modelo de colorização de Gouraud
    glShadeModel(GL_SMOOTH)
    
    
          
    #load objetos
    # Objetos baixados gratuitamente de alguns sites (não criei  os objetos, apenas editei e fiz load no projeto)
    


    caixinha = OBJ(PATH+'open-cardboard-box.obj', swapyz=False, my_texture = False, use_mat = False)
    bola = OBJ(PATH+'cube_m.obj', swapyz=False, my_texture=False, use_mat = False)
    
    
    base = OBJ(PATH+'base_bm.obj', swapyz=False, my_texture=False, use_mat = False)
    ombro = OBJ(PATH+'shoulder_b.obj', swapyz=False, my_texture=False, use_mat = False)
    bicep = OBJ(PATH+'bicep_b.obj', swapyz=False, my_texture=False, use_mat = False)
    bicep001 = OBJ(PATH+'bicep001_b.obj', swapyz=False, my_texture=False, use_mat = False)
    pulso = OBJ(PATH+'wrist_b.obj', swapyz=False, my_texture=False, use_mat = False)
    suport_pinca = OBJ(PATH+'grail_b.obj', swapyz=False, my_texture=False, use_mat = False)
    pinca = OBJ(PATH+'gripper_b.obj', swapyz=False, my_texture=False, use_mat = False)
    pinca001 = OBJ(PATH+'gripper001_b.obj', swapyz=False, my_texture=False, use_mat = False)
    cubo = OBJ(PATH+'sphere.obj', swapyz=False, my_texture=False, use_mat = True)

    texturabraco = loadTexture('telhado-2.jpeg')
    
    clock = pygame.time.Clock()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, game.width/float(game.height), 1, 2000.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW) 
    glEnable(GL_COLOR_MATERIAL)
    
    #inicial sequencia para o braco apartir desta o restante será calculada 
    sequencia_inicial()
 

def sequencia_inicial():
    cine_inv.sequencia[0]= Poligono(circ2.x, circ2.y, circ2.z - cine_inv.offset.z, 
                        angulos_pinca[contador], cine_inv.distancia_salto) 
    # posicao da bola 
    cine_inv.sequencia[1] = Poligono(circ2.x, circ2.y, circ2.z - cine_inv.offset.z, 
                        angulos_pinca[contador], 0) 
    #pinça proxima da bola
    cine_inv.sequencia[2] = cine_inv.sequencia[1]
    
    #posição de lançamento da bola
    cine_inv.sequencia[3] = Poligono(cine_inv.ponto.x, cine_inv.ponto.y, cine_inv.ponto.z- 
                        cine_inv.offset.z+10, angulos_pinca[contador], 0)
    #posição para soltar a bola e ela ser relançada 
    cine_inv.sequencia[4] = Poligono(sequencia_inicial.drop_loc.x, sequencia_inicial.drop_loc.y, 
                        sequencia_inicial.drop_loc.z, sequencia_inicial.drop_loc.angulo, cine_inv.distancia_salto)
    #posicao desoltar
    cine_inv.sequencia[5] = Poligono(sequencia_inicial.drop_loc.x, sequencia_inicial.drop_loc.y, 
                        sequencia_inicial.drop_loc.z, sequencia_inicial.drop_loc.angulo,0)

    cine_inv.sequencia[6] = cine_inv.sequencia[5]
    
    cine_inv.sequencia[7] = cine_inv.sequencia[4]
    
sequencia_inicial.drop_loc = Poligono(.0001,-250.0, -70, -45) 


def set_specular():
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT)
    glColor(.2, .2, .2)
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
    glColor(.3,1,.1) 
    glColorMaterial(GL_FRONT_AND_BACK, GL_SPECULAR)
    glColor(.75,.75,.75)
    glColorMaterial(GL_FRONT_AND_BACK, GL_EMISSION)
    glColor(.1,.1,.1)
    glMaterial(GL_FRONT_AND_BACK, GL_SHININESS, 128 )

  
def clear_specular():
    glColorMaterial(GL_FRONT, GL_SPECULAR)
    glColor(.0,.0,.0)
    glColorMaterial(GL_FRONT, GL_EMISSION)
    glColor(.0,.0,.0)
    glMaterial(GL_FRONT, GL_SHININESS, 128 )

  
def renderizar_braco():    
    glBindTexture ( GL_TEXTURE_2D, texturabraco );
    glEnable(GL_NORMALIZE)
    
    glPushMatrix()
    glColor(1,1,1)     
    set_specular()
    glRotate(-90, 1, 0, 0)
    glTranslate(-99.5, -131, 0)  
    glCallList(base.gl_list)  
    glPushMatrix()
    
    
    ombro_rotacao(angulo[0])
    bicep_rotacao(angulo[1])
    bicep001_rotacao(angulo[2])
    pulso_rotacao(angulo[3])
    
    
    if cine_inv.bola_presa == True:#checar se está com a bola capturada 
        glPushMatrix()
        glPushAttrib(GL_CURRENT_BIT)
        glPushAttrib(GL_LIGHTING_BIT)
        
        glTranslate(circ2.x,circ2.y,circ2.z)
        glRotate(-cine_inv.angulo, 0,0,1) 
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)
        glColor(0,.3,.0) #Se a bola estiver capturada mudar a cor da bola
        clear_specular()
        glCallList(cubo.gl_list)
        
        glPopAttrib()
        glPopAttrib()
        glPopMatrix()
    
    pinca_mov(angulo[4])
    
    glPopMatrix()
    glPopMatrix()
    glDisable(GL_NORMALIZE);
    glDisable(GL_TEXTURE_2D);



 
 
def renderizar_bola():
    if cine_inv.bola_presa == False:
        if cine_inv.colisao == False:
            glColorMaterial(GL_FRONT, GL_DIFFUSE)
            glColor(.8,.0,.0) 
        else:
            glColorMaterial(GL_FRONT, GL_DIFFUSE)
            glColor(.0,.0,.5) 
        clear_specular()
        glPushMatrix()
        glTranslate(circ2.x,circ2.z,circ2.y) 
        glCallList(cubo.gl_list)
        glPopMatrix()
        

def agarrar_bola():
    global cine_inv
    #verificar se objeto está proximo o suficiente para fechar pinça.
    cine_inv.colisao = colisao_bola(cine_inv.ponto , cine_inv.raio_distancia, circ2, r2)      
    #fechar pinça
    cine_inv.ponto.x, cine_inv.ponto.y, cine_inv.ponto.z, cine_inv.angulo= Braco_coord.change_in_joints(angulo)
    cine_inv.ponto.z += cine_inv.offset.z
    

def set_angulos():
    global angulo

    if nova_angulos.done == False:
        angulo = nova_angulos.get_next() 


def atualizar_sequencia():
    global nova_sequencia, angulo   
    
    if cine_inv.nova_seq == 0 or cine_inv.nova_seq == 6:
        angulo[4] = 0 
    elif cine_inv.nova_seq == 2:
        angulo[4] = 5 
            
   
    cine_inv.sequencia[0].setar_cordenadas(circ2.x, circ2.y, circ2.z - cine_inv.offset.z, angulos_pinca[contador], cine_inv.distancia_salto) 
   
    cine_inv.sequencia[1].setar_cordenadas(circ2.x, circ2.y, circ2.z - cine_inv.offset.z, angulos_pinca[contador], 0) 
   
    cine_inv.sequencia[2] = cine_inv.sequencia[1]
    #bola na caixa posicao 
    cine_inv.sequencia[3].setar_cordenadas(cine_inv.ponto.x, cine_inv.ponto.y, cine_inv.ponto.z- cine_inv.offset.z+10, angulos_pinca[contador], 0)

    nova_sequencia = cine_inv.sequencia[cine_inv.nova_seq]


def calc_nova_bola_cord():
    global cine_inv, circ2
    
    #verifica se a bola não está presa
    if(cine_inv.bola_presa == False):
        
        #verifica se a bola está  proxima da caixa
        
        cine_inv.soltou_na_caixa = colisao_bola(cordenada_caixa , caixa_raio_distancia, circ2, r2)

        
        if cine_inv.soltou_na_caixa: # se estiver calcula uma posição random para resoltar a bola 
            
            circ2.setar_cordenadas(random.randrange(-210,210,1.0), random.randrange(20,210,1.0),123.5)  
 
# obtém a próxima sequencia                 
def move_sequencia():
    global cine_inv, contador, nova_angulos
    
    error, myA = Braco_coord.calc_positions(nova_sequencia.x,nova_sequencia.y, nova_sequencia.z, nova_sequencia.angulo, nova_sequencia.pounce)#200, 131.75
    # checa se a soltagem da bola ocorreu corretamente
    if error != True:
        nova_angulos.set_angulos(angulo, myA)
        cine_inv.nova_seq = (cine_inv.nova_seq+1)%len(cine_inv.sequencia)
        
    else:#angulo da pinca
        contador +=1
        if contador >= angulos_pinca.size:
            contador = 0  

           
def calc_angulo(a, speed=1):
    a=a*speed
    if a>360:
        a-=360
    return a  


def ombro_rotacao(a=0):
    
    glTranslate(99, 131.75, 87.4)
    
    glRotatef(a, 0.0, 0, 1)
    
    glTranslate(-99, -131.75, -87.4)
    
    glCallList(ombro.gl_list)
    
def bicep_rotacao(a=0):
    
    glTranslate(99, 131.75, 128.9)
    
    glRotatef(a, .98052, -0.1964, 0)
    
    glTranslate(-99, -131.75, -128.9)
    
    glCallList(bicep.gl_list)
    
def bicep001_rotacao(a=0):
    
    glTranslate(105.11, 162.26, 230.96)
    
    glRotatef(a, .98052,-0.1964, 0)
    glTranslate(-105.11, -162.26, -230.96)
    
    glCallList(bicep001.gl_list)
    
def pulso_rotacao(a=0):
    
    glTranslate(86.6, 70.3, 180.29)
    
    glRotatef(a, .98052,  -0.1964, 0)
    
    glTranslate(-86.6, -70.3, -180.29)
    
    glCallList(pulso.gl_list)
    glCallList(suport_pinca.gl_list)
    
def pinca_mov(a=0):
    
    global cine_inv, circ2
    
    glTranslate(a*.9805, a*-0.1964, 0)
    
    glCallList(pinca.gl_list)
    glTranslate(-a*1.961,  a*0.3928, 0)
    glCallList(pinca001.gl_list)
    if a < 4 and cine_inv.bola_presa == True:
        circ2.setar_cordenadas(cine_inv.ponto.x, cine_inv.ponto.y, cine_inv.ponto.z)
        cine_inv.bola_presa = False
        
    if a > 4.0 and cine_inv.colisao == True: 
        
        cine_inv.bola_presa = True  
        #atualizar posicao
        circ2.setar_cordenadas(bola_presa_cordenada.x, bola_presa_cordenada.y, bola_presa_cordenada.z) 
       


def display():
    global  enter_apertado
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    #setar posicao da  camera 
    control(0.1,0.1, mouse_down)
    
    #atualizar 
    agarrar_bola()
    
    #viewport/ camera
    atualizar_camera()
    
    #transladando  a caixa para o ponto de recebimento da bolinha e aumentando o tamanho  
    
    


    
    
    # salvar atributos iniciais
    glPushAttrib(GL_CURRENT_BIT)
    
    glPushAttrib(GL_LIGHTING_BIT)
    #glEnable(GL_NORMALIZE)
    #glCullFace(GL_FRONT)
    #glColor3f(1,1,1)
    renderizar_braco()
    #glDisable(GL_NORMALIZE);
    #glCullFace(GL_BACK)
      

    renderizar_bola()
    
  

    glPushMatrix()
    glScalef(2,2,2);
    glTranslatef(-10, 25, -130)
    glCallList(caixinha.gl_list)
    glPopMatrix()
    
    #chao
    glPushMatrix()	
    glColor3f(0.8,0.4,0.0)
    glTranslatef(-10, 20, -130)
    glRotatef(90, 1.0, 0.0,0.0)
    glRectf(-10000, -10000, 10000, 10000);
    glPopMatrix()
    
    glPopAttrib() 
    glPopAttrib()
    

    
    
    if enter_apertado == 1:
        atualizar_sequencia()
        #caminho automatico  até a bola 
        move_sequencia()
        enter_apertado = 0
        
    #Nova cordenada da bola de forma randomica   
    calc_nova_bola_cord()
    set_angulos()


class main():
    def __init__(self):
        self.run_game()
    
    def run_game(self):
        global mouse_down, enter_apertado
        init()
        while 1:
            clock.tick(30) 
            for e in pygame.event.get():
                if e.type == QUIT:
                    sys.exit()
        
                elif e.type == KEYDOWN:
                    if e.key == K_ESCAPE:
                        sys.exit() 
                    elif e.key == K_q:
                        button[0] = 1
                    elif e.key == K_w:
                        button[1] = 1
                    elif e.key == K_e:
                        button[2] = 1
                    elif e.key == K_s:
                        button[3] = 1
                    elif e.key == K_RETURN:
                            enter_apertado = 1                     
                
                elif e.type == KEYUP:
                    
                    if e.key == K_ESCAPE:# ao precionar esc sai do  programa
                        sys.exit() 
                    elif e.key == K_q:
                        button[0] = 0
                    elif e.key == K_w:
                        button[1] = 0
                    elif e.key == K_e:
                        button[2] = 0
                    elif e.key == K_s:
                        button[3] = 0
                    elif e.key == K_RETURN:
                        enter_apertado = 0
                            
                elif e.type == MOUSEBUTTONUP:
                    pygame.mouse.set_visible(True)
                    mouse_down = False
                elif e.type == MOUSEBUTTONDOWN:
                    mouse_down = True
            
            a_s = a_b = a_b001= a_w = a_g = 0
            kp = pygame.key.get_pressed()
            if kp[pygame.K_F1]:
                a_s = 1
            if kp[pygame.K_1]:
                a_s = -1
            if kp[pygame.K_F2]:
                a_b = 1
            if kp[pygame.K_2]:
                a_b = -1
            if kp[pygame.K_F3]:
                a_b001 = 1
            if kp[pygame.K_3]:
                a_b001 = -1
            if kp[pygame.K_F4]:
                a_w = 1
            if kp[pygame.K_4]:
                a_w = -1
            if kp[pygame.K_a]:
                a_g = 1
            if kp[pygame.K_d]:
                a_g = -1 
    
            #rotação 
            angulo[0] += calc_angulo(a_s)
            angulo[1] += calc_angulo(a_b)
            angulo[2] += calc_angulo(a_b001)
            angulo[3] += calc_angulo(a_w)
            angulo[4] += calc_angulo(a_g) 
            if angulo[4] > 17:
                angulo[4]=17
            elif angulo[4] < 1:
                angulo[4] = 1  
            
            display()                            
            pygame.display.flip()
    
            

if __name__ == "__main__":
    mane = main()
  
