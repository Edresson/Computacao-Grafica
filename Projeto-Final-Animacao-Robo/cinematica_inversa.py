#!/usr/bin/env python
# coding: utf8
'''
contém toda a lógica para a cinemática inversa.
créditos:
Logica para cinemática inversa:
https://maquinapensante.com/2016/01/31/simplified-inverse-kinematics-model-for-a-5-degree-of-freedom-gripper-robotic-arm-2011/

Exemplo aplicado da logica usando python projeto raspberrypi:

Project: 3D Robot Simulator IK  disponivel em: https://www.raspberrypi.org/forums/viewtopic.php?f=41&t=34300&p=291674#p291674
para achar procure na pagina (ctrl+f) por  Project: 3D Robot Simulator IK , pois se trata de um repositorio com varios tutoriais

deixei o Arquivo baixado, está na pasta do projeto denominada exemplo_cinematica_inversa.py
'''

import numpy as np
import math

#Classe armazenará a posição dos objetos
class Poligono():  
    def __init__(self, x, y, z, angulo=0.0, pounce = 0.0): 
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.angulo = angulo
        self.pounce = pounce
        
    def setar_cordenadas(self, x, y, z, angulo=0, pounce =0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.angulo = angulo
        self.pounce = pounce
        
    def get_cord(self):
        return self.x, self.y, self.z
    
class cordenadas():
    def __init__(self):
        
        self.ponto = Poligono(200, 131.75, 0)
        
        self.offset = Poligono(0,0,127.5)
        
        self.raio_distancia = 4
        self.angulo = 283
        self.bola_presa = False
        self.colisao = False
        self.soltou_na_caixa = False
        
        self.distancia_salto = 40
       
        self.sequencia = list([Poligono(0.0,0.0,0.0)]*8)#listade sequencia
        self.nova_seq = 0
          
class plot_angulos():
    '''retirada do exemplo'''
    def __init__(self, start, finish):
        self.speed = 1
        self.counter = 0
        self.iter = 0
        self.start = start
        self.finish = finish
        self.delta_a = np.array([0.0]*5,dtype=float)
        self.distance = np.array([0.0]*5,dtype=float) 
        self.done = False
        self.close_gripper = False
        for i in range(5):
            if start[i]==0:
                start[i]=.0001
            if finish[i]==0:
                start[i]=.0001
        self.calc_pos()
        
    def set_angulos(self, start, finish):
        self.start = start
        self.finish = finish
        self.done = False
        for i in range(5):
            if start[i]==0:
                start[i]=.0001
            if finish[i]==0:
                start[i]=.0001
        self.calc_pos()
           
    def calc_pos(self):
        self.distances = np.add(self.finish, -self.start)
        self.distances[0] = self.distances[0]%360
        if self.distances[0] > 180:
            self.distances[0] = self.distances[0] - 360
        if self.distances[0] < -180:
            self.distances[0] = self.distances[0] + 360 
        
        if self.close_gripper == False:    
            self.distances[4] = 0.0000001
        else:
            self.distances[4] = 5
        
        self.test_limits()
        self.iter = np.max(abs(self.distances))
        
        if self.iter != 0:
            for i, angulo in enumerate(self.distances):
                self.delta_a[i] = angulo / self.iter
                        
    def get_next(self):
        if self.counter < self.iter:
            self.counter += 1
            self.new_angulo = np.add(self.start, np.multiply(self.delta_a, self.counter))
            ##print self.counter
            return self.new_angulo
        else:
            self.counter = 0
            self.done = True
            return self.new_angulo  
              
    def test_limits(self):
        
        start_angulo = (np.array([11.5, 108, 45, 28, 0]))
        for i in range(5):
            
            if (start_angulo[i] + self.distances[i]) > 180:
                pass
                
            if (start_angulo[i] + self.distances[i]) < -180:
                pass
                


class Cordenadas_bracoMec(object):
    def __init__(self, init_slider=list([0]*5)):
        SEGMENTS = int(5) #number of phantomX segments
        SLIDER_HOME = init_slider
        SLIDER_HOME[0] = 281.5 #starting angulo
        
        #initial settings of sliders, could pass these?
        self.tw = SLIDER_HOME[1] # w axis position depth
        self.tz = SLIDER_HOME[2]# z axis starting position height
        self.gripper_angulo = SLIDER_HOME[3] #preselected gripper angulos
        self.gripper = SLIDER_HOME[4]
  
        #variables used to calculate data
        self.l12 = 0.0 # hypotenuse belween a1 & a3
        self.a12 = 0.0 #inscribed angulo between hypotenuse, w 
        self.w = np.array([0]*SEGMENTS,dtype=float) #horizontal Poligono
        self.z = np.array([0]*SEGMENTS,dtype=float) #vertical Poligono
        self.x = np.array([0]*SEGMENTS,dtype=float) #x axis components 
        self.y = np.array([0]*SEGMENTS,dtype=float) #y axis components
        self.sliders_val = np.array([0]*SEGMENTS,dtype=float)
        
        self.l = np.array([0, 105, 105, 98])# actual measurements of segment length in mm        
        self.a = np.array([SLIDER_HOME[0]]*SEGMENTS,dtype=float) #angulo for the link, reference is previous link
        
        #temp
        self.Joints_tw = 0
        self.joints_l12 = 0
        self.joints_tool_angulo  = 0
        
    def angulos_to_toolponto(self, angulos): 
        tool_angulo = angulos[1]+angulos[2]+angulos[3]
        self.joints_tool_angulo = tool_angulo 
        l12 = math.sqrt((self.l[1]*self.l[1])+(self.l[2]*self.l[2])
                      -(2*self.l[1]*self.l[2]*math.cos(angulos[2])))
        
        if angulos[2]%(6.2831853) > math.pi: #the other side of the triangulo
            l12 = -l12

        if l12 > 210:#this should not be possible
            pass
               
        
        if self.l[1]*l12 != 0:#don't divide by 0
            sigma = math.acos(((self.l[1]*self.l[1])+(l12*l12)
                        -(self.l[2]*self.l[2])) / (2*self.l[1]*l12))
        else:
            sigma = 0
            
        a12 = angulos[1]-sigma
        self.joints_l12 = l12
        w2 = l12*math.cos(a12)
        z2 = l12*math.sin(a12)
        wt = (self.l[3]*math.cos(tool_angulo))+w2
        zt = (self.l[3]*math.sin(tool_angulo))+z2
        
        return wt, zt #tool ponto
          
    def change_in_joints(self, an):#281.5, 108, 45, 208, 0
        start_angulo = (np.array([281.5, 108, 45, 208, 0]))
        an = np.deg2rad(np.add(-an, start_angulo))
        
        t_w, t_z = self.angulos_to_toolponto(an)
        self.Joints_tw = t_w

        
        t_x = t_w*math.cos(an[0])
        t_y = t_w*math.sin(an[0])
        return -t_x, -t_y, t_z, math.degrees(an[0])
                
    def calc_p2(self):#calculates position 2
        self.w[3] = self.tw
        self.z[3] = self.tz
        self.w[2] = self.tw-np.cos(np.radians(self.gripper_angulo))*self.l[3]
        self.z[2] = self.tz-np.sin(np.radians(self.gripper_angulo))*self.l[3]
        
        self.l12 = np.sqrt(np.square(self.w[2])+np.square(self.z[2])) 
        if self.l12 > (self.l[1]+self.l)[2]:
            pass
            
           
    def calc_p1(self):#calculate position 1
        self.a12 = np.arctan2(self.z[2],self.w[2])#return the appropriate quadrant  
        self.a[1] = np.arccos((np.square(self.l[1])+np.square(self.l12)-np.square(self.l[2])) 
                              /(2*self.l[1]*self.l12))+self.a12
        self.w[1] = np.cos(self.a[1])*self.l[1]
        self.z[1] = np.sin(self.a[1])*self.l[1]
    
    def calc_angulos(self): #calculate all of the motor angulos see diagram
        self.a[2] = np.arctan((self.z[2]-self.z[1])/(self.w[2]-self.w[1]))-self.a[1]
        self.a[3] = np.deg2rad(self.gripper_angulo)-self.a[1]-self.a[2]  

    def calc_x_y(self):#calc x_y of servos Poligonos 
        for i in range(4):#fixed number of segments
            self.x[i] = self.w[i]*np.cos(self.a[0])
            self.y[i] = self.w[i]*np.sin(self.a[0])
    
    #recieves final position and calculates all join angulos         
    def calc_positions(self, t_x, t_y, t_z, g_a, pounce=0):#no swap because robot is rotated
        error = False
        
        if t_x ==0:
            
            a0=.00001
        else:
            a0 = math.atan(t_y / t_x )
        if t_x >= 0 and t_y >= 0:#first quadrant starting angulo i
            pass
            
        elif t_x <= 0 and t_y >= 0:#second quadrant tan is negative + 90
            
            a0 = a0 + 3.14159
        elif t_x <= 0 and t_y <= 0:#third quadrant tan is positive     
            
            a0 = a0 + 3.14159 #78.5
        elif t_x >= 0 and t_y <= 0:#fourth quadrant it should be negative
            pass
            
        else :
            
            pass
            
        self.a[0] = a0
        
        
        
        self.tw = math.sqrt((t_x*t_x) + (t_y*t_y)) - pounce
        self.tz = t_z + pounce
        self.gripper_angulo  = g_a 
        self.a[4] = self.gripper_angulo 
        
        self.calc_p2() 
        self.calc_p1() 
        self.calc_x_y()
        self.calc_angulos() 
        
        start_angulo = (np.array([101.5, 108, -135, 28, 0]))#coord -360 + 180
        angulo = np.add(-np.rad2deg(self.a), start_angulo)
        
        
        if self.l12 > (self.l[1]+self.l)[2]:
            
            error = True
        return  error, angulo
    

    
