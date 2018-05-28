from  Modulos.Ponto import *
import numpy as np
class Ponto3D(Ponto):
    
    
    def __init__(self,x,y,z):
       Ponto.__init__(self, x, y)
       self.z = z
        
    def calc_VetMat3D(self,b):

        c = [0, 0, 0,0]

        a = [self.x, self.y,self.z, 1]
        for i in range(0, 4):
            for j in range(0, 4):
                c[i] = c[i] + a[j] * b[j][i]

        self.x = c[0]
        self.y = c[1]
        self.z = c[2]


        
        '''a = [[self.x],[self.y],[self.z],[1]]
        c =np.dot(np.array(b),np.array(a))
        print(c)
        self.x = float(c[0])
        self.y=float(c[1])
        self.z = float(c[2])'''
