import math
import numpy as np

class Poligono(object):
    def __init__(self) :
        self.pontos = []
        self.Id = 0
        self.tipo = ""
        
    def desenha(Canvas) :
        pass
    def DDA(self,x1,y1,x2,y2):
        
            x =x1
            y=y1
            

            lista = []
            if(abs(( x2 - x1)) >= abs((y2- y1))):
               length = abs((x2- x1 ))
            else:
               length = abs(( y2 - y1))
               
            deltax = float (( x2 - x1))/ float(length)
            deltay = float (( y2- y1))/ float(length)

            for i in range(int(length)):
               
                x = x + deltax;
                y = y+ deltay;
                lista.append([x,y])
            return lista
		

    def bresenham(self,start, end):
    

                
                    start = list(start)
                    end = list(end)
                    lista = []
                    
                    steep = abs(end[1]-start[1]) > abs(end[0]-start[0])
                    
                    if steep:
                            start = swap(start[0],start[1])
                            end = swap(end[0],end[1])
                    
                    if start[0] > end[0]:
                            
                            _x0 = int(start[0])
                            _x1 = int(end[0])
                            start[0] = _x1
                            end[0] = _x0
                            
                            _y0 = int(start[1])
                            _y1 = int(end[1])
                            start[1] = _y1
                            end[1] = _y0
                    
                    dx = end[0] - start[0]
                    dy = abs(end[1] - start[1])
                    error = 0
                    derr = dy/float(dx)
                    
                    ystep = 0
                    y = start[1]
                    
                    if start[1] < end[1]: ystep = 1
                    else: ystep = -1
                    
                    for x in range(int(start[0]),int(end[0])+1):
                            if steep:
                                    lista.append((y,x))
                            else:
                                    lista.append((x,y))
                            
                            error += derr
                            
                            if error >= 0.5:
                                    y += ystep
                                    error -= 1.0
                    
                    return lista
    def transformadas(self,operacao,fatorx=None,fatory=None,fatorz=None):
        """1- Translação
        2- Escalonamento Homogenio
        3- Escalonamento 
        4- Rotação
        5- Rotação Homogenia
        6- Reflexao"""
        self.c=0        
        if operacao == 2 or operacao == 5:
            if self.tipo =="3D":
                self.pt = PontoCentral3D(self.pontos)
            else:
                
                self.pt = PontoCentral(self.pontos)
            
            
        for i in self.pontos:
        
            if operacao == 1:
                if self.tipo =="3D":
                     self.c=matrizTrans3D(fatorx,fatory,fatorz)
                else:   
                   self.c=matrizTrans(fatorx,fatory)
                   #lista = Translate(i.x,i.y,m

            elif operacao == 2:
                if self.tipo =="3D":
                    self.c = matrizesc3D(fatorx, fatory, fatorz)
                    """self.c = matrizTrans3D(-1*self.pt[0], -1*self.pt[1],-1*self.pt[2])
                    #self.c = matrizesc3D(fatorx, fatory, fatorz)
                    self.c = calc_Matriz(self.c, matrizesc3D(fatorx, fatory,fatorz));
                    self.c = matrizTrans3D(self.pt[0], self.pt[1], self.pt[2])"""
                    
                    
                else:
                    self.c = matrizTrans(-1*self.pt[0], -1*self.pt[1])
                    #self.c = matrizesc(fatorx, fatory)
                    self.c = calc_Matriz(self.c, matrizesc(fatorx, fatory));
                    self.c = calc_Matriz(self.c, matrizTrans(self.pt[0],self.pt[1]))
                    
            elif operacao == 3:
                
                if self.tipo =="3D":
                    self.c = matrizesc3D(fatorx, fatory,fatorz)
                else:
            
                    self.c = matrizesc(fatorx, fatory)
                
            elif operacao == 4:
                if self.tipo =="3D":

                    if fatorx != None:
                        self.c = matrizrot3Dx(fatorx)
                    elif fatory != None :
                        self.c = matrizrot3Dy(fatory)
                    elif fatorz != None:
                        self.c = matrizrot3Dz(fatorz)




                    #self.c =matrizrot3D(fatorx)
                else:
               
                    self.c =matrizrot(fatorx)
                
            elif operacao == 5:
                if self.tipo =="3D":
                    if fatorx != None:
                        self.c = matrizTrans3D(-1 * self.pt[0], -1 * self.pt[1], -1 * self.pt[2])
                        self.c = calc_Matriz(self.c, matrizrot3Dx(fatorx));
                        self.c = calc_Matriz(self.c, matrizTrans3D(self.pt[0], self.pt[1], self.pt[2]))
                        #self.c = matrizTrans3D(-1 * self.pt[0], -1 * self.pt[1],-1 * self.pt[2])
                        #self.c = matrizrot3Dx(fatorx)
                        #self.c = calc_Matriz(self.c, matrizrot3Dx(fatorx));
                        #self.c = calc_Matriz(self.c, matrizTrans3D(self.pt[0], self.pt[1], self.pt[2]))

                    elif fatory != None :
                        self.c = matrizTrans3D(-1 * self.pt[0], -1 * self.pt[1], -1 * self.pt[2])
                        self.c = calc_Matriz(self.c, matrizrot3Dy(fatory));
                        self.c = calc_Matriz(self.c, matrizTrans3D(self.pt[0], self.pt[1], self.pt[2]))
                        #self.c = matrizTrans3D(-1 * self.pt[0], -1 * self.pt[1], -1 * self.pt[2])
                        #self.c = calc_Matriz(self.c, matrizrot3Dy(fatory));
                        #self.c = matrizrot3Dy(fatory)
                        #self.c = calc_Matriz(self.c, matrizTrans3D(self.pt[0], self.pt[1], self.pt[2]))
                    elif fatorz != None :
                        #self.c = matrizrot3Dz(fatorz)

                        self.c = matrizTrans3D(-1 * self.pt[0], -1 * self.pt[1], -1 * self.pt[2])
                        self.c = calc_Matriz(self.c, matrizrot3Dz(fatorz));
                        self.c = calc_Matriz(self.c, matrizTrans3D(self.pt[0], self.pt[1], self.pt[2]))

                else:
                    
                    self.c = matrizTrans(-1*self.pt[0], -1*self.pt[1])
                    self.c = calc_Matriz(self.c, matrizrot(fatorx));
                    self.c = calc_Matriz(self.c, matrizTrans(self.pt[0],self.pt[1]))
                     
            elif operacao == 6:
                if self.tipo =="3D":
                    pass
                else:
                    
                    #self.c = matrizTrans(-1*self.pt[0], -1*self.pt[1])
                    self.c = matrizrefle(fatorx)
                    #self.c = calc_Matriz(self.c, matrizTrans(self.pt[0],self.pt[1]))
            if self.tipo =="3D":
                #if self.c != 0:

                    i.calc_VetMat3D(self.c)
            else:

                i.calc_VetMat(self.c)
        
def Cohen_Sutherland(clipping, ponto1,ponto2):
            xmin = clipping.xmin
            ymax = clipping.ymax
            xmax = clipping.xmax
            ymin = clipping.ymin
            x1= ponto1.x
            y1= ponto1.y
            x2= ponto2.x
            y2= ponto2.y
    
            Dentro,Esquerda, Direita, Baixo, Cima = 0,1, 2, 4, 8

            

            # checar posicao do clip
            posicaoP1 = ponto1.PosicaoClip(clipping,x1, y1)
            posicaoP2 =ponto2.PosicaoClip(clipping,x2, y2) 


            while(posicaoP1 | posicaoP2)!= 0: # Se Ambos estiverem Dentro (0000) aceita facil resolução

                if (posicaoP1 & posicaoP2) != 0: #Se estiver fora da janela clipping retorna a lista [0,0,0,0]
                    return [0, 0, 0, 0]

                #Caso dificil um dos pontos estão fora da janela clipping e outro esta dentro.

                posicao = posicaoP1 or posicaoP2 #pega o primeiro ponto que não seja zero,
                if posicao & Cima: #se a posição do ponto estiver acima
                    x = x1 + (x2-x1)*(ymax-y1)/(y2-y1)
                    y = ymax
                elif posicao & Baixo:#se a posição do ponto estiver abaixo
                    x = x1+(x2-x1)*(ymin-y1)/(y2 - y1)
                    y = ymin
                elif posicao & Direita:#se a posição do ponto estiver a Direita
                    y = y1+(y2-y1)*(xmax-x1)/(x2-x1)
                    x = xmax
                elif posicao & Esquerda:
                    y = y1+(y2-y1)*(xmin-x1)/(x2-x1)#se a posição do ponto estiver a Esquerda
                    x = xmin

                if posicao == posicaoP1:#Atualização da posição clip
                    x1, y1 = x, y
                    posicaoP1 = ponto1.PosicaoClip(clipping,x1, y1)
                    
                elif posicao == posicaoP2:
                    x2, y2 = x, y
                    posicaoP2 =ponto2.PosicaoClip(clipping,x2, y2)
            
            return [x1, y1, x2, y2]
    

        
         

                
def swap(n1,n2):
		return [n2,n1]

	    
def DesenhaCircunferencia(xc,yc,r):
            x=0
            y=r
            lista = []
            lista.append([xc,yc,x,y])
            
            p = 1-r
            while x < y :
                if p < 0:
                    x=x+0.05
                else:
                    x=x+0.05
                    y = y-0.05

                if p < 0:
                    p = p+2*x +0.05
                else:
                    p = p + 2 * (x -y ) +0.05
                lista.append([xc,yc,x,y])
                

            return lista


def deCasteljau(points, u, k = None, i = None, dim = None):
    
    if k == None: 
        k = len(points)-1
        i = 0
        dim = len(points[0])

    
    if k == 0:
        return points[i]

    a = deCasteljau(points, u, k = k-1, i = i, dim = dim)
    b = deCasteljau(points, u, k = k-1, i = i+1, dim = dim)
    result = []

    
    for j in range(dim):
        result.append((1-u) * a[j] + u * b[j])

    return result


def Hermite(p1,p2,p3,p4):
    time = 0
    data = list() 
    tx1 = p2[0] - p1[0]
    ty1 = p2[1]-p1[1]
    t1 = [tx1,ty1]
    tx2 = p4[0] - p3[0]
    ty2 = p4[1]-p3[1]
    t2 = [tx2,ty2]

    
    while time < 1.01:
      t= time


      b0 = 2*t*t*t - 3*t*t + 1

      b1 = -2*t*t*t + 3*t*t
      b2 = t*t*t - 2*t*t + t
      b3 = t*t*t - t*t
  
      x = b0*p1[0] + b1*p4[0] + b2*t1[0]+ b3*t2[0]
      y = b0*p1[1] + b1*p4[1] + b2*t1[1] + b3*t2[1]
      try:
          z = b0*p1[2] + b1*p4[2] + b2*t1[2] + b3*t4[2]
      except:
          z =0
      p = [x,y,z]
      data.append(p)
      time = time + .01

    return data




def bezier( p1, p2, p3, p4):
        def bezier_t( t, w):
        
            t2 = t * t
            t3 = t2 * t
            mt = 1-t
            mt2 = mt * mt
            mt3 = mt2 * mt
            return w[0]*mt3 + 3*w[1]*mt2*t + 3*w[2]*mt*t2 + w[3]*t3
        t = 0
        lista = []
        
        while (t < 1):
            x = bezier_t(t, (p1[0], p2[0], p3[0], p4[0]))
            y = bezier_t(t, (p1[1], p2[1], p3[1], p4[1]))
            #print(x)
            
         
            lista.append([math.floor(x), math.floor(y)])
            t += 0.001
            #print (t)
        return lista
            

def b_spline(p):
        M = [ [-1/6,3/6,-3/6,1/6],[3/6,-6/6,3/6,0],[-3/6,0,3/6,0],[1/6,4/6,1/6,0]]
        #print(M)
        Gx= [[p[0][0]],[p[1][0]],[p[2][0]],[p[3][0]]]
        Gy  = [[p[0][1]],[p[1][1]],[p[2][1]],[p[3][1]]]
        MGX =np.dot(np.array(M),np.array(Gx))
        MGY =np.dot(np.array(M),np.array(Gy))
        #print(MGY)
        #print(MGX)
        
        def b_spline_C(t,G):
            t2= t*t
            t3 = t2*t
            T = [ t3,t2,t,1]
             
            val = np.dot(np.array(T),G)
            #print("t",T)
            #print("val",val)
            
            return val
            
            

            

        t = 0
        lista = []
        
        while (t <= 1):
        #for k in np.linspace(0,1,100):
            
            x = b_spline_C(t,MGX)
            y = b_spline_C(t,MGY)
                #print(x)
                    
            lista.append([math.floor(x), math.floor(y)])
            
            t += 0.001
            #print (t)
        return lista



def b_spline_forward(p,t):
        def desenhacurvafwd(n,x,dx,ddx,dddx,y,dy,ddy,dddy):
            i=0
            pontos = []
            while( i <= n):
                i = i+1
                x=x+dx
                dx = dx+ddx
                ddx = ddx+dddx
                y = y + dy
                dy = dy+ddy
                ddy = ddy+dddy
              

                pontos.append([x,y])
                
            return pontos

        


        M = [ [-1/6,3/6,-3/6,1/6],[3/6,-6/6,3/6,0],[-3/6,0,3/6,0],[1/6,4/6,1/6,0]]
        #print(M)
        Gx= [[p[0][0]],[p[1][0]],[p[2][0]],[p[3][0]]]
        Gy  = [[p[0][1]],[p[1][1]],[p[2][1]],[p[3][1]]]
        valx =np.dot(np.array(M),np.array(Gx))
        valy =np.dot(np.array(M),np.array(Gy))
        
        lista = [] 
        delta = t
        delta2 = delta*delta
        delta3 = delta2*delta

        # matriz de forward differences
        x =[valx[3],
            valx[0]*delta3+valx[1]*delta2+valx[2]*delta,
            6*valx[0]*delta3+2*valx[1]*delta2,
            6*valx[0]*delta3]
        y =[valy[3],
            valy[0]*delta3+valy[1]*delta2+valy[2]*delta,
            6*valy[0]*delta3+2*valy[1]*delta2,
            6*valy[0]*delta3]

        
        lista = desenhacurvafwd(100,x[0],x[1],x[2],x[3],y[0],y[1],y[2],y[3])        
        
        return lista


    
    
    


    
def Translate (x,y,Tlist):
    
    return calc_VetMat( [x,y,1], Tlist)
    
def Escalonamento(x,y,sx,Elist):
    
    return calc_VetMat( [x,y,1], Elist)


def PontoCentral(pol):
    x=0
    y=0;
    ret = [0,0]
    for i in range(len(pol)):
       
        
        x= x+ pol[i].x
        y= y+ pol[i].y
		
    x = x/len(pol)
    y= y/len(pol) 
    ret[0] = x
    ret[1] = y
    
    return ret

def PontoCentral3D(pol):
    x=0
    y=0;
    z=0
    ret = [0,0,0]
    for i in range(len(pol)):
       
        z=z+pol[i].z
        x= x+ pol[i].x
        y= y+ pol[i].y
		
    x = x/len(pol)
    y= y/len(pol)
    z  = z/len(pol)
    ret[0] = x
    ret[1] = y
    ret[2] =z
    
    return ret






def calc_Matriz(a, b):
    #c = [[0,0,0],[0,0,0],[0,0,0]]
    A = np.array(a)
    B = np.array(b)
    C = np.dot(A,B)
    return C.tolist () 

def matrizTrans(dx, dy):

    return [[1,0,0], [0,1,0], [dx, dy, 1]]

def matrizTrans3D(dx, dy,dz):

    return [[1,0,0,0], [0,1,0,0], [0,0,1,0],[dx, dy,dz, 1]]
    
def matrizesc(sx, sy):

    return [[sx,0,0], [0,sy,0], [0, 0, 1]]

def matrizesc3D(sx, sy,sz):

    return [[sx,0,0,0], [0,sy,0,0], [0,0,sz,0],[0, 0,0, 1]]


def matrizrot(graus):
    
    Rlist = [ [math.cos(math.radians(graus)), math.sin(math.radians(graus)),0],[-1* math.sin(math.radians(graus)),math.cos(math.radians(graus)),0], [0, 0, 1]]
    return Rlist

def matrizrot3Dx(graus):
    
    Rlist = [ [1,0,0,0],[0,math.cos(math.radians(graus)), math.sin(math.radians(graus)),0],[0,-1* math.sin(math.radians(graus)),math.cos(math.radians(graus)),0], [0, 0,0, 1]]
    return Rlist


def matrizrot3Dy(graus):
    Rlist = [[math.cos(math.radians(graus)),0,-1*math.sin(math.radians(graus)), 0],
             [0,1,0,0],
             [ math.sin(math.radians(graus)),0, math.cos(math.radians(graus)), 0], [0, 0,0, 1]]
    return Rlist


def matrizrot3Dz(graus):
    Rlist = [[math.cos(math.radians(graus)), math.sin(math.radians(graus)), 0,0],
             [-1 * math.sin(math.radians(graus)), math.cos(math.radians(graus)), 0,0], [0, 0, 1,0],[0,0,0,1]]
    return Rlist



def matrizrefle(eixo):
    if eixo == 1:#eixox
        ret = [[1,0,0], [0,-1,0], [0, 0, 1]]
    elif eixo == 2:#eixoy
        ret = [[-1,0,0], [0,1,0], [0, 0, 1]]
    elif eixo == 3:#origem
        ret = [[-1,0,0], [0,-1,0], [0, 0, 1]] 
    return ret
    
    
    






    
