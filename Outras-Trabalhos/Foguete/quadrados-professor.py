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


# Tamanho do incremento nas direções x e y
# (número de pixels para se mover a cada
# intervalo de tempo)
xstep = 1.0;
ystep = 1.0;

# Largura e altura da janela
windowWidth = 0;
windowHeight= 0;


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
    global windowWidth, windowHeight, xstep, ystep, ang, x1, y1, rsize
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





     gluOrtho2D(0.0, windowWidth, 0.0, windowHeight);

def DesenhaFoguete():
    glClearColor(1.0,1.0,1.0,1.0)
    gl
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
glutDisplayFunc(Desenha);
glutReshapeFunc(AlteraTamanhoJanela);
glutTimerFunc(33, Timer, 1);
Inicializa();



glutMainLoop();

