from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import os


win = 50
largura = 0
altura = 0
aspecto = 0

def Desenha2():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def DesenhaCasa():
    print("desenho casa")
    #glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)  # vermelho
    glBegin(GL_QUADS)

    glVertex2f(-15.0, -15.0)
    glVertex2f(-15.0, 5.0)
    glVertex2f(15.0, 5.0)
    glVertex2f(15.0, -15.0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(-4.0, -14.0)
    glVertex2f(-4.0, 0.0)
    glVertex2f(4.0, 0.0)
    glVertex2f(4.0, -14.5)
    glVertex2f(7.0, -5.0)
    glVertex2f(7.0, -1.0)
    glVertex2f(13.0, -1.0)
    glVertex2f(13.0, -5.0)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)  # azul

    glBegin(GL_LINES)

    glVertex2f(7.0, -3.0)
    glVertex2f(13.0, -3.0)
    glVertex2f(10.0, -1.0)
    glVertex2f(10.0, -5.0)
    glEnd()
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-15.0, 5.0)
    glVertex2f(0.0, 17.0)
    glVertex2f(15.0, 5.0)

    glEnd()

    #glFlush()

def FazMoldura():
    global altura, largura, win,aspecto
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-win*aspecto, -win)
    glVertex2f(float(-win) * float(aspecto), float(win))
    glVertex2f(float(win) * float(aspecto),float( win))
    glVertex2f(float(win) * float(aspecto), float(-win))
    '''glVertex2f(-50,-50)
    glVertex2f(-50,50)
    glVertex2f(50,50)
    glVertex2f(50,-50)'''
    glEnd()
    glLineWidth(1)

def Desenha():
    global altura,largura

    glClear(GL_COLOR_BUFFER_BIT)

    glViewport(0,0,int(largura),int(altura))

    DesenhaCasa()
    FazMoldura()
    print(largura,altura)
    glViewport(int(largura),0,int(largura),int(altura))
    DesenhaCasa()
    FazMoldura()
    glFlush()


def Inicializa():
    glClearColor(0.0 ,0.0,0.0,1.0)


def teclado(tecla,x,y):
    if tecla == b'\x1b':
        #print("tchau")
        os._exit(0)
    elif tecla == b'a':
        glutFullScreen()

    elif tecla == b's':
        glutReshapeWindow(100,100)
        glutPositionWindow(500,500)
    else:

        print("vc apertou \n",tecla)



def teclasEspeciais(tecla,x,t):
    posx  = 300
    if tecla ==GLUT_KEY_F1:
        print("vc apertou f1")

    elif tecla== GLUT_KEY_LEFT:

        if(posx>50):
            posx=posx-50
        glutPositionWindow(posx,300)
    elif tecla == GLUT_KEY_RIGHT:

        if posx < 500:
            posx = posx+50
        glutPositionWindow(posx, 300)

    else:
        print('vc apertou outra tecla especial',tecla)


def GerenciaMouse(button,state,x,y):
    if state == GLUT_DOWN:
        print('botao ',button,'apertado')
    else:
        print('botao',button,' liberado')


def movimentoMouseBotatoApertado(x,y):
    pass
    print("botao apertado ",x,y)

def movimentoMouse(x,y):
    pass
    #print(x,y)


def ocioso():
    print('.')


def menucor(op):
    if int(op) == 0:
        glClearColor(1.0,0.0,0.0,1.0)

    elif int(op) == 1:
        glClearColor(0.0,1.0,0.0,1.0)
    elif int(op) == 2:
        glClearColor(0.0, 0.0, 1.0, 1.0)
    else:
        glClearColor(0.0, 0.0, 0.0, 1.0)

    glutPostRedisplay()

def criaMenu():
    menu = glutCreateMenu(menucor)
    glutAddMenuEntry('Vermelho',0)
    glutAddMenuEntry('Verde', 1)
    glutAddMenuEntry('Azul', 2)
    glutAddMenuEntry('Preto', 3)
    glutAttachMenu(GLUT_RIGHT_BUTTON)





def AlteraTamanhoJanela(w , h):
    global largura,altura,win,aspecto

    if h == 0:
        h=1
    #especifica as dimensoes da view port
    largura = w/2
    altura = h
    aspecto =float( largura/altura)


    #glViewport(0,0,w,h)

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()
    gluOrtho2D(-win*aspecto ,win*aspecto, -win,win)



glutInit()
displayMode = GLUT_RGB| GLUT_SINGLE;
glutInitDisplayMode (displayMode)
Inicializa()

glutCreateWindow("Primeiro Programa- Teclado")


glutSpecialFunc(teclasEspeciais)
glutKeyboardFunc(teclado)

glutMouseFunc(GerenciaMouse)
glutMotionFunc(movimentoMouseBotatoApertado)
glutPassiveMotionFunc(movimentoMouse)

#glutIdleFunc(ocioso)
criaMenu()


glutReshapeFunc(AlteraTamanhoJanela)
glutDisplayFunc(Desenha)


glutMainLoop()

