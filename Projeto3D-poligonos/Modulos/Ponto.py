import numpy as np

class Ponto(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def xw2Vp(self,vp,w):
        return (( self.x - w.xmin)/(w.xmax- w.xmin))*(vp.xmax - vp.xmin)
       
    
    def yw2Vp(self,vp,w):
        return  (1-(self.y - w.ymin)/(w.ymax- w.ymin))*(vp.ymax - vp.ymin)

    def calc_VetMat(self,b):
        c = [0,0,0]


        a = [self.x,self.y,1]
        for i in range(0,3):
            for j  in range(0,3):
                c[i] = c[i] +a[j] * b[j][i]
            
        self.x = c[0]
        self.y=c[1]
        
    def PosicaoClip(self,clipping,x,y):
        xmin = clipping.xmin
        ymax = clipping.ymax
        xmax = clipping.xmax
        ymin = clipping.ymin
        Dentro,Esquerda, Direita, Baixo, Cima = 0,1, 2, 4, 8
        p = Dentro  #no inicio tá dentro Dentro

        #considerando x
        if x < xmin:
            p |= Esquerda
        elif x > xmax:
            p |= Direita

        #considerando y
        if y < ymin:
            p |= Baixo 
        elif y > ymax:
            p |= Cima 
        return p
