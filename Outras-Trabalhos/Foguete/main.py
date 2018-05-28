# Anima.c - Isabel H. Manssour
# Um programa OpenGL simples que mostra a animação
# de quadrado em  uma janela GLUT.
# Este código está baseado no Bounce.c, exemplo
# disponível no livro "OpenGL SuperBible",
# 2nd Edition, de Richard S. e Wright Jr.

#include <windows.h>
#include <gl/gl.h>
#include <gl/glut.h>
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *


# Tamanho e posição inicial do quadrado
x1 = 100.0;
y1 = 150.0;
rsize = 50
ang = 0
angulo = 0
x3 =0
y3 =0
z3 =0
# Tamanho do incremento nas direções x e y
# (número de pixels para se mover a cada
# intervalo de tempo)
xstep = 1.0;
ystep = 1.0;

movimentando = 0
# Largura e altura da janela
windowWidth = 500;
windowHeight= 500;
texto = ''

def  DesennhaTexto(string):
    global rsize
    glColor3f(0.0, 1, 0, 0)
   # win = 500
    #win = windowHeight
    win = rsize
    #glClear()
    glPushMatrix()
    glRasterPos2f(-win,win-(win*0.08))
    for character in string:

            #print(character);

            #glutBitmapCharacter(GLUT.GLUT_BITMAP_TIMES_ROMAN_10,string[i])
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10, ord(character));

    glPopMatrix()
    #glEnd()

def MoveMouse(x,y):

    global texto
    texto = '(' + str(x) + ',' + str(y) + ')'
    glutPostRedisplay()


# Função callback chamada para fazer o desenho
def Desenha():
     global windowWidth,windowHeight,xstep,ystep,ang,x1,y1,rsize
     glMatrixMode(GL_MODELVIEW);
     glLoadIdentity();
     # Limpa a janela de visualização com a cor de fundo especificada
     glClear(GL_COLOR_BUFFER_BIT);
     glColor3f(0.0, 1.0, 1.0);
     glTranslatef(100,100,0);
     ang= ang+1
     glRotatef(ang,0,0,1);
     glBegin(GL_QUADS);
     glVertex2f(50,50);
     glVertex2f(50,0);
     glVertex2f(0,0);
     glVertex2f(0,50);
     glEnd();

     glLoadIdentity();


     # Especifica que a cor corrente é vermelha
     #         R     G     B
     glColor3f(1.0, 0.0, 0.0);

     # Desenha um quadrado preenchido com a cor corrente
     glBegin(GL_QUADS);
     glVertex2f(x1,y1+rsize);
     glVertex2f(x1,y1);
     # Especifica que a cor corrente é azul
     glColor3f(0.0, 0.0, 1.0);
     glVertex2f(x1+rsize,y1);
     glVertex2f(x1+rsize,y1+rsize);
     glEnd();

     # Executa os comandos OpenGL
     #glutSwapBuffers(); # é o flush para imagens bufferizadas
     glFlush();


# Função callback chamada pela GLUT a cada intervalo de tempo
# (a window não está sendo redimensionada ou movida)
def Timer(value):
    global movimentando
    global windowWidth, windowHeight, xstep, ystep, angulo, x3, y3, rsize
    x1 = x3
    y1 = y3
    ang =angulo
    # Muda a direção quando chega na borda esquerda ou direita
    if(x1 > windowWidth-rsize or x1 < 0):
        xstep = -xstep;
    # Muda a direção quando chega na borda superior ou inferior
    if(y1 > windowHeight-rsize or y1 < 0):
        
        ystep = -ystep;
    # Verifica as bordas.  Se a window for menor e o
    # quadrado sair do volume de visualização
    if(x1 > windowWidth-rsize):
         x1 = windowWidth-rsize-1;
    if(y1 > windowHeight-rsize):
        
         y1 = windowHeight-rsize-1;
     # Move o quadrado
    x1 = float(x1+float(xstep));
    #print(xstep,ystep)
    y1 = float(y1 +float(ystep));

    x3 =x1
    y3 = y1
    if(movimentando == 1):
    # Redesenha o quadrado com as novas coordenadas
        glutPostRedisplay();
        glutTimerFunc(33,Timer, 1);


# Inicializa parâmetros de rendering
def Inicializa ():
    # Define a cor de fundo da janela de visualização como preta
    glClearColor(0.0, 0.0, 0.0, 1.0);

# Função callback chamada quando o tamanho da janela é alterado
def AlteraTamanhoJanela( w, h):



     # Evita a divisao por zero
     global windowWidth, windowHeight, xstep, ystep, ang, x1, y1, rsize
     if(h == 0):
         h = 1;

     # Especifica as dimensões da Viewport
     glViewport(0, 0, w, h);

     # Inicializa o sistema de coordenadas
     glMatrixMode(GL_PROJECTION);
     glLoadIdentity();

     # Estabelece a janela de seleção (left, right, bottom, top)
     if (w <= h):

         windowHeight = 250.0*h/w;
         windowWidth = 250.0;
     else:
        windowWidth = 250.0 * w / h;
        windowHeight = 250.0;




     print(windowWidth, windowHeight)
     gluOrtho2D(0.0, windowWidth, 0.0, windowHeight);

def Bico():
    #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    #glLoadIdentity()
    glColor3f(0.0,0.0,0,1)
    glTranslatef(130,250,0)
    glBegin(GL_TRIANGLES)

    glVertex3f(0.0, 30.0, 0.0)
    glVertex3f(-30.0, -30.0, 0.0)
    glVertex3f(30.0, -30.0, 0.0)
    glEnd()


def Corpo():
    #glLoadIdentity()
    glColor3f(0.0, 0.0,1, 0)
    glTranslatef(0, -130, 0)
    glBegin(GL_QUADS);

    glVertex2f(-30, 100);
    glVertex2f(30, 100);
    glVertex2f(30, -100);
    glVertex2f(-30, -100);
    glEnd();
    pass



def AsaEsquerda():
    glColor3f(0.0, 1, 0, 0)
    glTranslatef(-30, -80, 0)
    glBegin(GL_TRIANGLES)

    glVertex3f(0.0, 20.0, 0.0)
    glVertex3f(-20.0, -20.0, 0.0)
    glVertex3f(0.0, -20.0, 0.0)
    glEnd()
    pass

def  AsaDireita():
    glColor3f(0.0, 1, 0, 0)
    glTranslatef(60, 0, 0)
    glBegin(GL_TRIANGLES)

    glVertex3f(0.0, 20.0, 0.0)
    glVertex3f(20.0, -20.0, 0.0)
    glVertex3f(0.0, -20.0, 0.0)
    glEnd()

    pass


def DesenhaFoguete():
    #print('aqui')
    global texto
    global angulo,x3,y3,z3

    glClearColor(1.0,1.0,1.0,1.0)

    glClear(GL_COLOR_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity()

    glRotatef(angulo, 0, 0, 1);
    glTranslatef(x3, y3, z3);



    Bico()
    Corpo()
    AsaEsquerda()
    AsaDireita()
    DesennhaTexto(texto)
    glFlush()

def GerenciaMouse(button, state, x, y):
        global angulo,movimentando
        print('botao ', button, 'apertado')

        if state == GLUT_DOWN:
            if int(button) == 0:
                angulo = angulo +10
                movimentando = 0
                glutPostRedisplay();

            elif int(button) == 2:
                angulo = angulo -10
                movimentando = 0
                glutPostRedisplay();
            elif int(button) == 1:
                movimentando = 1
                glutTimerFunc(33, Timer, 1);
                #angulo = angulo -10
                #glutPostRedisplay();

            print(angulo)
        else:
            pass
            #print('botao', button, ' liberado')

def teclasEspeciais(tecla,x,t):
    global x3,y3,z3


    if tecla== GLUT_KEY_LEFT:
        x3 = x3+10
        glutPostRedisplay();
        pass

    elif tecla == GLUT_KEY_RIGHT:

        x3 = x3 - 10
        glutPostRedisplay();
        pass

    elif tecla == 101:

        y3 = y3 + 10
        glutPostRedisplay();
        pass

    elif tecla == 103:

        y3 = y3 - 10
        glutPostRedisplay();
        pass

    else:
        print('vc apertou outra tecla especial',tecla)



# Programa Principal
#int main(void)

# glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);

glutInit()
displayMode = GLUT_SINGLE | GLUT_RGB
glutInitDisplayMode (displayMode)



#glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
glutInitWindowSize(400,350);
glutInitWindowPosition(10,10);
glutCreateWindow("Anima");
glutDisplayFunc(DesenhaFoguete);
glutReshapeFunc(AlteraTamanhoJanela);

glutPassiveMotionFunc(MoveMouse)
#glutTimerFunc(33, Timer, 1);
Inicializa();

glutMouseFunc(GerenciaMouse)
glutSpecialFunc(teclasEspeciais)



glutMainLoop();

