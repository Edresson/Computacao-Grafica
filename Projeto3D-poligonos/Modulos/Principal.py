# ui to py : pyuic5 -x interface.ui  -o Interface.py
try:
    import Modulos.Interface as qt
    from  Modulos.Ponto import *
    from  Modulos.Ponto3D import *
    from  Modulos.Janela import *
    from  Modulos.Poligono import *
    from  Modulos.DisplayFile import *
    
except:
    import Interface as qt
    from  Ponto import *
    from  Ponto3D import *
    from  Janela import *
    from  Poligono import *
    from  DisplayFile import *
    
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen,QCursor
from PyQt5 import QtCore
import copy
import time
import time


from  PyQt5.QtWidgets import QFileDialog   
class Principal(QWidget):
    def __init__(self,Form, ui ):

        super().__init__(Form)
        self.ui = ui
        self.ultimoid = 0;

        self.Realeasecordenada = False
        self.Presscordenada = False
        
        self.clipp = False
        self.clippingP = []

        #bezier
        self.bezierp = 0 
        self.bspline = 0 
        self.pontosh = []
        self.bsplinespontos =[]
        
        self.reta_x_fim = 0.0
        self.reta_y_fim = 0.0
        self.reta_x_inicio = 0.0
        self.reta_y_inicio = 0.0
        self.setGeometry(180, 70, 500, 500)
        #self.setGeometry(-250, -250, 250, 250)
        #self.setWindowTitle('Points')
        
        p = self.palette()
        self.setMouseTracking(True)
        p.setColor(self.backgroundRole(),QtCore.Qt.white)
        self.setPalette(p)
        self.setAutoFillBackground(True)
        self.setPalette(p)

        
        
        self.viewport = Janela(0,0,500,500)
        self.mundo = Janela(-250,-250,250,250)
        self.clipping = Janela(-100,-100,100,100)
        
        self.update_pinBox_Mundo()
        #self.qp.drawLine(250, 0, 250,500)
        #self.qp.drawLine(0,250, 0,250)

        
        self.poliAux = Poligono ()
        self.display = DisplayFile()
        

        
        
        #adicionei o eixo vertical
        self.poliAux.pontos.append( Ponto(0,self.mundo.ymax))
        self.poliAux.pontos.append( Ponto(0,self.mundo.ymin))
        self.poliAux.Id = self.ultimoid
        self.ultimoid += 1
        self.poliAux.tipo="LineTo"
        
        self.display.poligonos.append( copy.copy(self.poliAux))
        
        self.poliAux.pontos =[]



        #adicionei o eixo horizontal
        self.poliAux.pontos.append( Ponto(self.mundo.xmin,0))
        self.poliAux.pontos.append( Ponto(self.mundo.xmax,0))
        self.poliAux.Id = self.ultimoid
        self.ultimoid += 1
        self.poliAux.tipo="LineTo"
        self.display.poligonos.append( copy.copy(self.poliAux))

        self.poliAux.pontos =[]


       
        
        self.updatecanvas()
        self.show()
    """ --------------------------------------------------------"""

    #Metodos de Movimentação/navegação na viewport
    
    """ --------------------------------------------------------"""

    def ClippingPoligonos(self):
            
            
            self.clippingAux= []
            self.ultimoaux = 0
            self.ui.PushButton_Clipping.setText("UnClipping")
            self.poliAux.pontos =[]
            #adicionei reta clipping 1 
            self.poliAux.pontos.append( Ponto(-100,100))
            self.poliAux.pontos.append( Ponto(100,100))
            self.poliAux.Id = self.ultimoaux
            self.ultimoaux += 1
            self.poliAux.tipo="LineTo"
            self.clippingAux.append( copy.copy(self.poliAux))
            self.poliAux.pontos =[]
            #adicionei reta  clipping 2
            self.poliAux.pontos.append( Ponto(100,-100))
            self.poliAux.pontos.append( Ponto(-100,-100))
            self.poliAux.Id = self.ultimoaux
            self.ultimoaux  += 1
            self.poliAux.tipo="LineTo"
            self.clippingAux.append( copy.copy(self.poliAux))
            self.poliAux.pontos =[]
            #adicionei reta clipping 3
            self.poliAux.pontos.append( Ponto(-100,100))
            self.poliAux.pontos.append( Ponto(-100,-100))
            self.poliAux.Id = self.ultimoaux
            self.ultimoaux += 1
            self.poliAux.tipo="LineTo"
            self.clippingAux.append( copy.copy(self.poliAux))
            self.poliAux.pontos =[]
            #adicionei  reta clipping 3
            self.poliAux.pontos.append( Ponto(100,100))
            self.poliAux.pontos.append( Ponto(100,-100))
            self.poliAux.Id = self.ultimoaux
            self.ultimoaux += 1
            self.poliAux.tipo="LineTo"
            self.clippingAux.append( copy.copy(self.poliAux))
            self.poliAux.pontos =[]
            
            ### Tratando os pontos
            
            for i in self.display.poligonos:# Percorrendo a Lista Poligonos que é um atributo da classe display
                    
                    if str(i.tipo) == "DDA" or str(i.tipo)  == "Bresenham" or str(i.tipo) == "LineTo" : # verificando o tipo do poligono! ### função elif equivale a função else if . 
                            
                        self.list = []
                        k = 0
                        while k <  len( i.pontos)-1:
                            
                            lista = Cohen_Sutherland(self.clipping,i.pontos[k],i.pontos[k+1])
                            
                            if lista != [0,0,0,0]:
                                
                                self.list.append(lista)
                                
                            k = k+1
                        
                        
                        for j in self.list:                
                                self.poliAux.pontos.append( Ponto(j[0],j[1]))
                                self.poliAux.pontos.append( Ponto(j[2],j[3]))

                        self.poliAux.Id = self.ultimoaux
                        self.ultimoaux += 1
                        self.poliAux.tipo=str(i.tipo)
                        self.clippingAux.append( copy.copy(self.poliAux))
                        self.poliAux.pontos =[]


                        



                    elif str(i.tipo) == "Hermite"  or str(i.tipo) == "Bezier"   or str(i.tipo) ==  "deCasteljau" or str(i.tipo) == "B-Splines" or str(i.tipo) ==  "B-Splines-Forward":
                        
                        self.poliAux.pontos =[]
                        test = []
                        lista = [] 
                        test = i.pontos
                        
                        k = 0
                        
                        while k < len(test)-1:
                            posicao = test[k].PosicaoClip(self.clipping,test[k].x,test[k].y)
                            
                            if(posicao ==0):
                                
                                lista.append([test[k].x,test[k].y])
                            
                            k = k+1
                        

                        for j in lista:
                            self.poliAux.pontos.append( Ponto(j[0],j[1]))
                        
                        self.poliAux.Id = self.ultimoaux
                        self.ultimoaux += 1
                        self.poliAux.tipo=str(i.tipo) 
                        self.clippingAux.append( copy.copy(self.poliAux))
                        self.poliAux.pontos =[]

                        
                    elif str(i.tipo) =="Circunferência":
                        l=0
                        lista = []
                        while l < len (i.pontos)-1:
                            posicao = i.pontos[l].PosicaoClip(self.clipping,i.pontos[l].x,i.pontos[l].y)
                            if(posicao ==0):
                                lista.append([i.pontos[l].x,i.pontos[l].y])
                                
                            l=l+1
                        for i in lista:
                            self.poliAux.pontos.append( Ponto(i[0],i[1]))
                        
                        self.poliAux.Id = self.ultimoaux
                        self.ultimoaux += 1
                        self.poliAux.tipo="Circunferência"
                        self.clippingAux.append( copy.copy(self.poliAux))
                        self.poliAux.pontos =[]  

                        

            self.display.poligonos = self.clippingAux            
            self.update()
            
    def Clipping(self) :
        #print(self.clipp)
        if self.clipp == False:
            self.clipp =True
            self.clippingP = copy.copy(self.display.poligonos)

            self.ClippingPoligonos()

        else:
            
            self.clipp =False
            self.Clear()
            
            self.display.poligonos=self.clippingP
                    
            self.clippingP = []
            
            self.ui.PushButton_Clipping.setText("Clipping")
            self.update()
            
    
        
    def Subir(self) :
        porcentagem = int(self.ui.spinBox_zoom.value())
        if str(self.ui.comboBox_zoom.currentText()) == "Valor":
            
            self.mundo.ymax =  self.mundo.ymax + porcentagem
            self.mundo.ymin =  self.mundo.ymin + porcentagem
        else:
            self.mundo.ymax =  self.mundo.ymax + (self.mundo.ymax/100)*porcentagem
            #self.mundo.ymin =  self.mundo.ymin - (self.mundo.ymin/100)*porcentagem
        
        self.Update_Eixos()
        
    def Descer(self) :
        porcentagem = int(self.ui.spinBox_zoom.value())
        if str(self.ui.comboBox_zoom.currentText()) == "Valor":
            self.mundo.ymin =  self.mundo.ymin - porcentagem
            self.mundo.ymax =  self.mundo.ymax - porcentagem
        else:
            
            self.mundo.ymax =  self.mundo.ymax -(self.mundo.ymax/100)*porcentagem
            #self.mundo.ymin =  self.mundo.ymin + (self.mundo.ymin/100)*porcentagem
        self.Update_Eixos()
        
    def Esquerda(self) :
        porcentagem = int(self.ui.spinBox_zoom.value())
        if str(self.ui.comboBox_zoom.currentText()) == "Valor":
            self.mundo.xmax =  self.mundo.xmax + porcentagem
            self.mundo.xmin =  self.mundo.xmin + porcentagem
        else:
            self.mundo.xmax =  self.mundo.xmax + (self.mundo.xmax/100)*porcentagem
            #self.mundo.xmin =  self.mundo.xmin - (self.mundo.xmin/100)*porcentagem
        self.Update_Eixos()
        
    def Direita(self) :
        porcentagem = int(self.ui.spinBox_zoom.value())
        if str(self.ui.comboBox_zoom.currentText()) == "Valor":
            self.mundo.xmax =  self.mundo.xmax - porcentagem
            self.mundo.xmin =  self.mundo.xmin - porcentagem
        else:
            
            self.mundo.xmax =  self.mundo.xmax - (self.mundo.xmax/100)*porcentagem
            #self.mundo.xmin =  self.mundo.xmin + (self.mundo.xmin/100)*porcentagem
        self.Update_Eixos()
        
    def ZoomMais (self) :
        porcentagem = self.ui.spinBox_zoom.value()
        
        if str(self.ui.comboBox_zoom.currentText()) == "Valor":
            self.mundo.xmax =  self.mundo.xmax - porcentagem
            self.mundo.ymax =  self.mundo.ymax - porcentagem
            self.mundo.xmin =  self.mundo.xmin + porcentagem
            self.mundo.ymin =  self.mundo.ymin + porcentagem
        else:
            self.mundo.xmax =  self.mundo.xmax - (self.mundo.xmax/100)*porcentagem
            self.mundo.ymax =  self.mundo.ymax - (self.mundo.ymax/100)*porcentagem
            self.mundo.xmin =  self.mundo.xmin - (self.mundo.xmin/100)*porcentagem
            self.mundo.ymin =  self.mundo.ymin - (self.mundo.ymin/100)*porcentagem
        self.Update_Eixos()
            
    def ZoomMenos (self) :
        porcentagem = self.ui.spinBox_zoom.value()
        
        if str(self.ui.comboBox_zoom.currentText()) == "Valor":
            self.mundo.xmax =  self.mundo.xmax +  porcentagem
            self.mundo.ymax =  self.mundo.ymax +  porcentagem
            self.mundo.xmin =  self.mundo.xmin -  porcentagem
            self.mundo.ymin =  self.mundo.ymin -  porcentagem
            
        else:
            self.mundo.xmax =  self.mundo.xmax +  (self.mundo.xmax/100)*porcentagem
            self.mundo.ymax =  self.mundo.ymax +  (self.mundo.ymax/100)*porcentagem
            self.mundo.xmin =  self.mundo.xmin +  (self.mundo.xmin/100)*porcentagem
            self.mundo.ymin =  self.mundo.ymin +  (self.mundo.ymin/100)*porcentagem
        self.Update_Eixos()


    """ --------------------------------------------------------"""

     #Metodos de Atualização Canvas[Qpainter]. 
    
    """ --------------------------------------------------------"""

    def paintEvent(self, e):
        """ --------------------------------------------------------------------------------------------------"""
        #Como nome já diz este é o Metodo de Pintura, este metodo é responsavel pela Plotagem de todos os tipos de poligonos,
        #Em Qt é apenas possivel atualizar o Canvas[Qpainter] usando este metodo!
        """ --------------------------------------------------------------------------------------------------"""
        
        self.ui.listWidget_Poligonos.clear() 
        self.qp = qt.QtGui.QPainter()# Instanciando um objeto do tipo Qpainter onde será nossa area de Desenho.
        self.qp.begin(self)
        pen = QPen(QtCore.Qt.black,2)# Instanciando um objeto do tipo Caneta, setando sua cor para petra e fonte 2.s

        self.qp.setPen(pen)# Setando o objeto caneta instanciado para o objeto Qpainters

        if(self.Realeasecordenada == True and self.Presscordenada == True):
            self.Realeasecordenada = False
            self.Presscordenada = False
        try:
            for i in self.display.poligonos:# Percorrendo a Lista Poligonos que é um atributo da classe display

                    
                    if str(i.tipo) == "DDA" : # verificando o tipo do poligono! ### função elif equivale a função else if .
                
                        self.bezierp = 0
                        self.updatelistbox_poligonos(i.Id)
                        lista = i.DDA(i.pontos[0].xw2Vp(self.viewport,self.mundo),i.pontos[0].yw2Vp(self.viewport,self.mundo),i.pontos[1].xw2Vp(self.viewport,self.mundo),i.pontos[1].yw2Vp(self.viewport,self.mundo))
                        for a in lista:
                            self.qp.drawPoint(a[0],a[1])
                        
                    elif str(i.tipo)  == "Bresenham":
                        self.bezierp = 0
                        self.updatelistbox_poligonos(i.Id)
                        lista = i.bresenham([i.pontos[0].xw2Vp(self.viewport,self.mundo),i.pontos[0].yw2Vp(self.viewport,self.mundo)],[i.pontos[1].xw2Vp(self.viewport,self.mundo),i.pontos[1].yw2Vp(self.viewport,self.mundo)])
                        for a in lista:
                            self.qp.drawPoint(a[0],a[1])


                    elif str(i.tipo) == "pLineTo":
                        
                        self.bezierp = 0
                        self.updatelistbox_poligonos(i.Id)
                        k = 0
                        test = i.pontos
                        #print(len(test))
                        while k < (len(test)-1):
                                self.qp.drawLine(test[k].xw2Vp(self.viewport,self.mundo),test[k].yw2Vp(self.viewport,self.mundo),test[k+1].xw2Vp(self.viewport,self.mundo),test[k+1].yw2Vp(self.viewport,self.mundo))
                                k = k +1
                            
    

                        

                        
                    elif str(i.tipo) == "LineTo":        
                        self.updatelistbox_poligonos(i.Id)
                        self.qp.drawLine(i.pontos[0].xw2Vp(self.viewport,self.mundo),i.pontos[0].yw2Vp(self.viewport,self.mundo),i.pontos[1].xw2Vp(self.viewport,self.mundo),i.pontos[1].yw2Vp(self.viewport,self.mundo))
                    
                    elif str(i.tipo) =="Circunferência":
                        self.bezierp = 0
                        self.updatelistbox_poligonos(i.Id)
                        l=0
                        
                        while l < len (i.pontos)-1:
                            self.qp.drawPoint(i.pontos[l].xw2Vp(self.viewport,self.mundo),i.pontos[l].yw2Vp(self.viewport,self.mundo))
                            l=l+1
                    elif str(i.tipo) == "Poligono":
                        self.bezierp = 0
                        self.updatelistbox_poligonos(i.Id)
                        
                    elif str(i.tipo) =="3D" :
                            pen = QPen(QtCore.Qt.cyan,2)# Instanciando um objeto do tipo Caneta, setando sua cor para amarela e fonte 2.s
                            
                            self.qp.setPen(pen)

                            
                            #if(self.bezierp == 4):
                            
                            
                            self.bezierp =0  
                            self.updatelistbox_poligonos(i.Id)
                            #print([[i.pontos[0].xw2Vp(self.viewport,self.mundo),i.pontos[0].yw2Vp(self.viewport,self.mundo)],[i.pontos[1].xw2Vp(self.viewport,self.mundo),i.pontos[1].yw2Vp(self.viewport,self.mundo)],[i.pontos[2].xw2Vp(self.viewport,self.mundo),i.pontos[2].yw2Vp(self.viewport,self.mundo)],[i.pontos[3].xw2Vp(self.viewport,self.mundo),i.pontos[3].yw2Vp(self.viewport,self.mundo)]])
                            k = 0
                            test = i.pontos
                            #print(len(test))
                            while k < (len(test)-1):
                                self.qp.drawLine(test[k].xw2Vp(self.viewport,self.mundo),test[k].yw2Vp(self.viewport,self.mundo),test[k+1].xw2Vp(self.viewport,self.mundo),test[k+1].yw2Vp(self.viewport,self.mundo))
                                k = k +1
                                
                    elif str(i.tipo) =="Hermite" :
                            pen = QPen(QtCore.Qt.yellow,2)# Instanciando um objeto do tipo Caneta, setando sua cor para amarela e fonte 2.s
                            

                            self.qp.setPen(pen)

                            
                            #if(self.bezierp == 4):
                            
                            
                            self.bezierp =0  
                            self.updatelistbox_poligonos(i.Id)
                            #print([[i.pontos[0].xw2Vp(self.viewport,self.mundo),i.pontos[0].yw2Vp(self.viewport,self.mundo)],[i.pontos[1].xw2Vp(self.viewport,self.mundo),i.pontos[1].yw2Vp(self.viewport,self.mundo)],[i.pontos[2].xw2Vp(self.viewport,self.mundo),i.pontos[2].yw2Vp(self.viewport,self.mundo)],[i.pontos[3].xw2Vp(self.viewport,self.mundo),i.pontos[3].yw2Vp(self.viewport,self.mundo)]])
                            k = 0
                            test = i.pontos
                            while k < (len(test)-1):
                                self.qp.drawLine(test[k].xw2Vp(self.viewport,self.mundo),test[k].yw2Vp(self.viewport,self.mundo),test[k+1].xw2Vp(self.viewport,self.mundo),test[k+1].yw2Vp(self.viewport,self.mundo))
                                k = k +1
                    elif str(i.tipo) =="Bezier" :
                         
                            pen = QPen(QtCore.Qt.green,2)# Instanciando um objeto do tipo Caneta, setando sua cor para petra e fonte 2.s

                            self.qp.setPen(pen)

                            
                            #if(self.bezierp == 4):
                            
                            
                            self.bezierp =0  
                            self.updatelistbox_poligonos(i.Id)
                            #print([[i.pontos[0].xw2Vp(self.viewport,self.mundo),i.pontos[0].yw2Vp(self.viewport,self.mundo)],[i.pontos[1].xw2Vp(self.viewport,self.mundo),i.pontos[1].yw2Vp(self.viewport,self.mundo)],[i.pontos[2].xw2Vp(self.viewport,self.mundo),i.pontos[2].yw2Vp(self.viewport,self.mundo)],[i.pontos[3].xw2Vp(self.viewport,self.mundo),i.pontos[3].yw2Vp(self.viewport,self.mundo)]])
                            k = 0
                            test = i.pontos
                            while k < (len(test)-1):
                                self.qp.drawLine(test[k].xw2Vp(self.viewport,self.mundo),test[k].yw2Vp(self.viewport,self.mundo),test[k+1].xw2Vp(self.viewport,self.mundo),test[k+1].yw2Vp(self.viewport,self.mundo))
                                k = k +1
                                
                                

                    elif str(i.tipo) =="B-Splines" or str(i.tipo) =="B-Splines-Forward":
                        self.updatelistbox_poligonos(i.Id)
                        test = i.pontos
                        k=0
                        while k < (len(test)-1):
                                self.qp.drawLine(test[k].xw2Vp(self.viewport,self.mundo),test[k].yw2Vp(self.viewport,self.mundo),test[k+1].xw2Vp(self.viewport,self.mundo),test[k+1].yw2Vp(self.viewport,self.mundo))
                                k = k +1
                        
                                
                            
                    elif str(i.tipo) =="deCasteljau":
                            pen = QPen(QtCore.Qt.red,2)# Instanciando um objeto do tipo Caneta, setando sua cor para petra e fonte 2.s

                            self.qp.setPen(pen)

                            
                            #if(self.bezierp == 4):
                            
                            
                            self.bezierp =0  
                            self.updatelistbox_poligonos(i.Id)
                            #print([[i.pontos[0].xw2Vp(self.viewport,self.mundo),i.pontos[0].yw2Vp(self.viewport,self.mundo)],[i.pontos[1].xw2Vp(self.viewport,self.mundo),i.pontos[1].yw2Vp(self.viewport,self.mundo)],[i.pontos[2].xw2Vp(self.viewport,self.mundo),i.pontos[2].yw2Vp(self.viewport,self.mundo)],[i.pontos[3].xw2Vp(self.viewport,self.mundo),i.pontos[3].yw2Vp(self.viewport,self.mundo)]])
                            k = 0
                            test = i.pontos
                            while k < (len(test)-1):
                                self.qp.drawLine(test[k].xw2Vp(self.viewport,self.mundo),test[k].yw2Vp(self.viewport,self.mundo),test[k+1].xw2Vp(self.viewport,self.mundo),test[k+1].yw2Vp(self.viewport,self.mundo))
                                k = k +1

                    

                           
        except:#chegou ao limite do Zoom
            
            self.ZoomMenos()
            
            
    ##### TRANSFORMAÇÕES CLICKS BOTÃO ####
    def Translater (self) :
        if self.ui.listWidget_Poligonos.currentItem() != None :
            self.ui.label_mensagemdivisaoporzero.hide()


            if   self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].tipo == "3D":
                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(1, float(
                    self.ui.doubleSpinBox_dx.value()), float(self.ui.doubleSpinBox_dy.value()), float(self.ui.doubleSpinBox_dz.value()))
            else:
                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(1,float( self.ui.doubleSpinBox_dx.value()),float(self.ui.doubleSpinBox_dy.value()))
           
            self.update()
        else:
            self.ui.label_mensagemdivisaoporzero.setText("Selecione um Poligono para a Translação") 
            self.ui.label_mensagemdivisaoporzero.show()
    def EscaleHomo(self):
        if self.ui.listWidget_Poligonos.currentItem() != None :
            self.ui.label_mensagemdivisaoporzero.hide()
            
            if self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].tipo == "3D":
                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(2, float(
                    self.ui.doubleSpinBox_sx.value()), float(self.ui.doubleSpinBox_sy.value()), float(self.ui.doubleSpinBox_sz.value()))

            else:
                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(2,float( self.ui.doubleSpinBox_sx.value()),float(self.ui.doubleSpinBox_sy.value()))
            
        
            self.update()
        else:
            self.ui.label_mensagemdivisaoporzero.setText("Selecione um Poligono para o Escalonamento") 
            self.ui.label_mensagemdivisaoporzero.show()
    def Escale(self):
        if self.ui.listWidget_Poligonos.currentItem() != None :
            self.ui.label_mensagemdivisaoporzero.hide()
            self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(3,float( self.ui.doubleSpinBox_sx.value()),float(self.ui.doubleSpinBox_sy.value()),float(self.ui.doubleSpinBox_sz.value()))
            
        
            self.update()
        else:
            self.ui.label_mensagemdivisaoporzero.setText("Selecione um Poligono para o Escalonamento") 
            self.ui.label_mensagemdivisaoporzero.show()
            
    def RotacaoHomo(self):
        if self.ui.listWidget_Poligonos.currentItem() != None :

            if self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].tipo == "3D":

                    self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(5, float(
                        self.ui.doubleSpinBox_angulo.value()))
                    time.sleep(0.2)
                    self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(5,None, float(
                        self.ui.doubleSpinBox_anguloy.value()))
                    time.sleep(0.2)
                    self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(5, None,None,float(
                        self.ui.doubleSpinBox_anguloz.value()))




            else:

                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(5,float( self.ui.doubleSpinBox_angulo.value()))

            self.ui.label_mensagemdivisaoporzero.hide()
            self.update()
        else:
            self.ui.label_mensagemdivisaoporzero.setText("Selecione um Poligono para a Rotacao") 
            self.ui.label_mensagemdivisaoporzero.show()
    def Rotacao(self):
        if self.ui.listWidget_Poligonos.currentItem() != None :
            self.ui.label_mensagemdivisaoporzero.hide()

            if self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].tipo == "3D":

                    self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(4, float(
                        self.ui.doubleSpinBox_angulo.value()))
                    time.sleep(0.2)
                    self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(4,None, float(
                        self.ui.doubleSpinBox_anguloy.value()))
                    time.sleep(0.2)
                    self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(4, None,None,float(
                        self.ui.doubleSpinBox_anguloz.value()))




            else:


                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(4,float( self.ui.doubleSpinBox_angulo.value()))
            
        
            self.update()
        else:
            self.ui.label_mensagemdivisaoporzero.setText("Selecione um Poligono para a Rotacao") 
            self.ui.label_mensagemdivisaoporzero.show()
            
    def Reflexao(self):
         if self.ui.listWidget_Poligonos.currentItem() != None :
            self.ui.label_mensagemdivisaoporzero.hide()
            if self.ui.radioButton_eixox.isChecked() == True:
                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(6,2)
            elif self.ui.radioButton_eixoy.isChecked() == True:
                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(6,1)
            else:# self.ui.radioButton_origem.isChecked() == True:
                self.display.poligonos[int(self.ui.listWidget_Poligonos.currentItem().text())].transformadas(6,3)
               
            self.update()
         else:
            self.ui.label_mensagemdivisaoporzero.setText("Selecione um Poligono para a Reflexão") 
            self.ui.label_mensagemdivisaoporzero.show()     
        
        
    def Clear(self) :
        """ --------------------------------------------------------"""

         #Metodos reponsavel por limpar o Qpainter, apagando todos os poligonos desenhados . 
    
        """ --------------------------------------------------------"""
        self.ui.listWidget_Poligonos_Tipo.clear()
        
        self.ultimoid = 0
        self.display.poligonos = []
        self.ui.listWidget_Pontos.clear()
        self.poliAux.pontos =[]
        #adicionei o eixo vertical
        self.poliAux.pontos.append( Ponto(0,self.mundo.ymax))
        self.poliAux.pontos.append( Ponto(0,self.mundo.ymin))
        self.poliAux.Id = self.ultimoid
        self.ultimoid += 1
        self.poliAux.tipo="LineTo"
        self.display.poligonos.append( copy.copy(self.poliAux))
        self.poliAux.pontos =[]
        #adicionei o eixo horizontal
        self.poliAux.pontos.append( Ponto(self.mundo.xmin,0))
        self.poliAux.pontos.append( Ponto(self.mundo.xmax,0))
        self.poliAux.Id = self.ultimoid
        self.ultimoid += 1
        self.poliAux.tipo="LineTo"
        self.display.poligonos.append( copy.copy(self.poliAux))
        
        self.poliAux.pontos =[]
        
        self.update()

    """ --------------------------------------------------------"""

     #Metodos de Captura das coordenadas do Mouse. 
    
    """ --------------------------------------------------------"""



    def mouseMoveEvent(self, event):
            """if self.Realeasecordenada == False and  self.Presscordenada == True:
                if str(self.ui.comboBox_Poligono.currentText()) == "Livre":
                    self.poliAux.pontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.poliAux.Id = self.ultimoid
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    self.update()"""
                    
                    
            
            self.updatelabelxy(event.x(),event.y(),self.XVp2w(event.x()),self.YVp2w(event.y()))
            
    
            
    def mousePressEvent(self, event):
            
            self.Presscordenada = True
            if str(self.ui.comboBox_Poligono.currentText()) == "DDA" or str(self.ui.comboBox_Poligono.currentText()) == "Bresenham" or str(self.ui.comboBox_Poligono.currentText()) == "LineTo"  or str(self.ui.comboBox_Poligono.currentText()) =="Circunferência":
                    #self.bezierp == 0 
                    self.poliAux.pontos =[]
                    self.poliAux.pontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))

                    
            if str(self.ui.comboBox_Poligono.currentText()) =="Poligono":
                if self.bezierp == 0 :
                    self.poliAux.pontos =[]
                    #self.bezierp = self.bezierp+1
                    self.poliAux.pontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.bezierp = self.bezierp+1
                    
                elif self.bezierp == 3 :
                    self.bezierp =0
    
                    self.poliAux.pontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.poliAux.Id = self.ultimoid
                    self.poliAux.tipo =  str("Poligono")
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    self.update()
                elif self.bezierp < 3:
                    
                    self.poliAux.pontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.bezierp = self.bezierp+1

            if str(self.ui.comboBox_Poligono.currentText()) =="B-Splines" or   str(self.ui.comboBox_Poligono.currentText()) =="B-Splines-Forward":
                
                if self.bspline == 0 :
                    self.bsplinespontos =[]
                    #self.bezierp = self.bezierp+1
                    self.bsplinespontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.bspline = self.bspline+1
                    
                """elif self.bspline == 3 :
                    self.bspline =0
    
                    self.poliAux.pontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.poliAux.Id = self.ultimoid
                    self.poliAux.tipo =  str("B-Splines")
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    self.update()
                elif self.bspline < 3:"""
                    
                self.bsplinespontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                self.bspline = self.bspline+1

                    
            if str(self.ui.comboBox_Poligono.currentText()) =="Hermite":
                
                if self.bezierp == 0 :
                    self.pontosh = [] 
                    #self.bezierp = self.bezierp+1
                elif self.bezierp == 3 :

                    self.pontosh.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    
                    
                    
                    self.bezierp = 0
                    test = Hermite([self.pontosh[0].x,self.pontosh[0].y],[self.pontosh[1].x,self.pontosh[1].y],[self.pontosh[2].x,self.pontosh[2].y],[self.pontosh[3].x,self.pontosh[3].y])
                            
                    
                    self.poliAux.pontos = []
                    for i  in test:
        
                        self.poliAux.pontos.append(Ponto(i[0],i[1]))

                        
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.comboBox_Poligono.currentText())
                   
                    self.ultimoid += 1
                    
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    
                    self.update()
                    
                if self.bezierp != 3: 
                    self.pontosh.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.bezierp = self.bezierp+1


                    
            if str(self.ui.comboBox_Poligono.currentText()) =="Bezier":
                
                if self.bezierp == 0 :
                    self.pontosh = [] 
                    self.poliAux.pontos =[]
                elif self.bezierp == 3 :
                    self.pontosh.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    
                    self.bezierp = 0
                    
                    test = bezier((self.pontosh[0].x,self.pontosh[0].y),(self.pontosh[1].x,self.pontosh[1].y),(self.pontosh[2].x,self.pontosh[2].y),(self.pontosh[3].x,self.pontosh[3].y))   
                    
                    
                    self.poliAux.pontos = []
                    for i  in test:
        
                        self.poliAux.pontos.append(Ponto(i[0],i[1]))
                        
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.comboBox_Poligono.currentText()) 
                    
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    
                    self.update()



                if self.bezierp != 3:
                    self.pontosh.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.bezierp = self.bezierp+1
                
                
            if str(self.ui.comboBox_Poligono.currentText()) =="deCasteljau":
                if self.bezierp == 0 :
                    self.pontosh = [] 
                    self.poliAux.pontos =[]
                elif self.bezierp == 3 :
                    self.pontosh.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    
                    self.bezierp = 0
                    curve =[]
                    for k in np.linspace(0,1,100):
                        curve.append(deCasteljau([[self.pontosh[0].x,self.pontosh[0].y],[self.pontosh[1].x,self.pontosh[1].y],[self.pontosh[2].x,self.pontosh[2].y],[self.pontosh[3].x,self.pontosh[3].y]],k))
                            
                    
                    self.poliAux.pontos = []
                    for i  in curve:
        
                        self.poliAux.pontos.append(Ponto(i[0],i[1]))
                        
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.comboBox_Poligono.currentText()) 
                    
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    
                    self.update()



                if self.bezierp != 3:
                    self.pontosh.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                    self.bezierp = self.bezierp+1
                    
                        

                    
                                
                    
    
    def mouseReleaseEvent(self, event):
        self.Realeasecordenada = True
        if (str(self.ui.comboBox_Poligono.currentText()) == "DDA"or str(self.ui.comboBox_Poligono.currentText()) == "Bresenham" or str(self.ui.comboBox_Poligono.currentText()) == "LineTo"):
                    
                    
                    
                    
                    if(self.XVp2w(event.x()) != self.poliAux.pontos[0].x and self.YVp2w(event.y())!= self.poliAux.pontos[0].y): # Se os dois pontos  não possuirem mesma cordenada  
                        self.poliAux.pontos.append( Ponto(self.XVp2w(event.x()),self.YVp2w(event.y())))
                        self.poliAux.Id = self.ultimoid
                        self.poliAux.tipo =  str(self.ui.comboBox_Poligono.currentText())
                        self.ultimoid += 1
                        self.display.poligonos.append( copy.copy(self.poliAux))
                        self.ui.label_mensagemdivisaoporzero.hide()
                    else:# Se tiverem a mesma cordenada avisar que o usuario deve clicar e arrastar o mouse não apenas clicar, isso também elimina o problema de divisão por zero nas retas !
                        self.ui.label_mensagemdivisaoporzero.setText("Clique e Arraste  Mouse ! Após precione Desenhar  ") 
                        self.ui.label_mensagemdivisaoporzero.show()
                    self.poliAux.pontos =[]
                    
        elif str(self.ui.comboBox_Poligono.currentText()) == "Circunferência":
            
                    lista = DesenhaCircunferencia(event.x(),event.y(),100)#Calculando os pontos da circunferencia , e atribuindo eles a uma lista . 
                    
                    for a in lista:#percorrendo a lista 
                        xc =a[0]
                        yc = a[1]
                        x = a[2]
                        y=a[3]
                        
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc),self.YVp2w(yc)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc+x),self.YVp2w(yc+y)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc+x),self.YVp2w(yc-y)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc-x),self.YVp2w(yc+y)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc-x),self.YVp2w(yc-y)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc+y),self.YVp2w(yc+x)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc+y),self.YVp2w(yc-x)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc-y),self.YVp2w(yc+x)))
                        self.poliAux.pontos.append(Ponto(self.XVp2w(xc-y),self.YVp2w(yc-x)))
                    
                        
                        
                    self.poliAux.Id = self.ultimoid
                    self.poliAux.tipo =  str(self.ui.comboBox_Poligono.currentText())
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))


    """ --------------------------------------------------------"""

     #Metodos de Atualizações, labels, eixos ,lista de poligonos , lista de pontos entre outros! . 
    
    """ --------------------------------------------------------"""
        
 

    def Press_ListPoligono_Tipo (self, index):
        if self.ui.listWidget_Poligonos.currentItem() != None  and self.ui.listWidget_Poligonos_Tipo.currentItem() != None :
            
            if str(self.ui.listWidget_Poligonos_Tipo.currentItem().text()) == "DDA" or str(self.ui.listWidget_Poligonos_Tipo.currentItem().text()) == "Bresenham"  or str(self.ui.listWidget_Poligonos_Tipo.currentItem().text()) == "LineTo":

                    self.k =int(self.ui.listWidget_Poligonos.currentItem().text())
                    
                    
                    self.display.poligonos[self.k].tipo = str(self.ui.listWidget_Poligonos_Tipo.currentItem().text())
                    self.update()
              
            if str(self.ui.listWidget_Poligonos_Tipo.currentItem().text())  =="deCasteljau":
                    self.k =int(self.ui.listWidget_Poligonos.currentItem().text())
                    i = self.display.poligonos[self.k]
                    
                    test =[]
                    self.pontosh = i.pontos
                    for k in np.linspace(0,1,100):
                        test.append(deCasteljau([[self.pontosh[0].x,self.pontosh[0].y],[self.pontosh[1].x,self.pontosh[1].y],[self.pontosh[2].x,self.pontosh[2].y],[self.pontosh[3].x,self.pontosh[3].y]],k))
                            
                    
                    self.poliAux.pontos = []
                    for i  in test:
        
                        self.poliAux.pontos.append(Ponto(i[0],i[1]))
                        
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.listWidget_Poligonos_Tipo.currentItem().text())
                    
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    
                    self.update()

                    
                    
            elif str(self.ui.listWidget_Poligonos_Tipo.currentItem().text()) == "Bezier" :
                    
                
                    self.k =int(self.ui.listWidget_Poligonos.currentItem().text())
                    i = self.display.poligonos[self.k]
                    test = bezier((i.pontos[0].x,i.pontos[0].y),(i.pontos[1].x,i.pontos[1].y),(i.pontos[2].x,i.pontos[2].y),(i.pontos[3].x,i.pontos[3].y))   
                    
                    
                    self.poliAux.pontos = []
                    for i  in test:
        
                        self.poliAux.pontos.append(Ponto(i[0],i[1]))
                        
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.listWidget_Poligonos_Tipo.currentItem().text())
                    
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    
                    self.update()
            elif str(self.ui.listWidget_Poligonos_Tipo.currentItem().text()) == "LineTo" :
                    self.k =int(self.ui.listWidget_Poligonos.currentItem().text())
                    i = self.display.poligonos[self.k]
                    
                    self.poliAux.pontos = []
                    for i  in i.pontos:
        
                        self.poliAux.pontos.append(Ponto(i[0],i[1]))
                        
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.listWidget_Poligonos_Tipo.currentItem().text())
                    
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                
                

                
            elif str(self.ui.listWidget_Poligonos_Tipo.currentItem().text()) == "Hermite" :
                    
                
                    self.k =int(self.ui.listWidget_Poligonos.currentItem().text())
                    i = self.display.poligonos[self.k]
                    test = Hermite([i.pontos[0].x,i.pontos[0].y],[i.pontos[1].x,i.pontos[1].y],[i.pontos[2].x,i.pontos[2].y],[i.pontos[3].x,i.pontos[3].y])
                            
                    
                    self.poliAux.pontos = []
                    for i  in test:
        
                        self.poliAux.pontos.append(Ponto(i[0],i[1]))
                        
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.listWidget_Poligonos_Tipo.currentItem().text())
                   
                    self.ultimoid += 1
                    self.display.poligonos.append( copy.copy(self.poliAux))
                    
                    self.update()

                    

    def updatelabelxy(self,xpos, ypos,xmundo,ymundo):
        self.ui.label_xyview.setText("("+ str(xpos)+"," + str(ypos)+")")
        self.ui.label_xymundo.setText("("+ str(float("{0:.3f}".format(xmundo)))+"," + str(float("{0:.2f}".format(ymundo)))+")")
        
    def browser_files(self):
        # global filedir
        File = QFileDialog()
        filedir = File.getOpenFileName()[0]

        arq = open(str(filedir), "r")

        lista = []
        for i in arq:
            pt = str(i).replace(']', '').replace("[", '').replace("\n", '')
            #print(pt)
            x, y, z = pt.split(',')
            lista.append([float(x), float(y), float(z)])

        self.poliAux.pontos = []
        for i in lista:

            self.poliAux.pontos.append(Ponto3D(i[0],i[1],i[2]))

        self.poliAux.Id = self.ultimoid
        self.poliAux.tipo = "3D"
        self.ultimoid += 1
        self.display.poligonos.append(copy.copy(self.poliAux))

        
    def Update_Eixos(self):
        #update eixo horizontal
        self.display.poligonos[0].pontos[0].y = self.mundo.ymax
        self.display.poligonos[0].pontos[1].y = self.mundo.ymin
        #update eixo vertical
        self.display.poligonos[1].pontos[1].x = self.mundo.xmax
        self.display.poligonos[1].pontos[0].x = self.mundo.xmin
        '''if self.clipp ==True:
            self.ClippingPoligonos()'''
        
        self.update()
    

    def update_pinBox_Mundo(self):
        self.ui.doubleSpinBox_mxmin.setValue(float(self.mundo.xmin))
        self.ui.doubleSpinBox_mxmax.setValue(float(self.mundo.xmax))
        self.ui.doubleSpinBox_mymin.setValue(float(self.mundo.ymin))
        self.ui.doubleSpinBox_mymax.setValue(float(self.mundo.ymax))
                
    def Set_Mundo_pinBox(self):
        self.mundo.xmin = self.ui.doubleSpinBox_mxmin.value()
        self.mundo.xmax = self.ui.doubleSpinBox_mxmax.value()
        self.mundo.ymax = self.ui.doubleSpinBox_mymax.value()
        self.mundo.ymin = self.ui.doubleSpinBox_mymin.value()
        self.Update_Eixos()
        self.update()
        
    def updatelistbox_poligonos(self,Id):
        self.ui.listWidget_Poligonos.addItem(str(Id))
        
    def updatelistbox_pontos(self,current, previous):
        if self.ui.listWidget_Poligonos.currentItem() != None :
            self.k =int(self.ui.listWidget_Poligonos.currentItem().text())
            self.ui.listWidget_Poligonos_Tipo.clear()
            
            if self.display.poligonos[self.k].tipo == "LineTo" or self.display.poligonos[self.k].tipo == "DDA" or self.display.poligonos[self.k].tipo == "Bresenham" :
                self.ui.listWidget_Poligonos_Tipo.addItem("LineTo")
                self.ui.listWidget_Poligonos_Tipo.addItem("DDA")
                self.ui.listWidget_Poligonos_Tipo.addItem("Bresenham")

            
            
                
            
            if self.display.poligonos[self.k].tipo == "Poligono":
                
                self.ui.listWidget_Poligonos_Tipo.addItem("Hermite")
                self.ui.listWidget_Poligonos_Tipo.addItem("Bezier")
                self.ui.listWidget_Poligonos_Tipo.addItem("deCasteljau")
                self.ui.listWidget_Poligonos_Tipo.addItem("LineTo")
            
            self.ui.listWidget_Pontos.clear()
            
            for i in self.display.poligonos[self.k].pontos:
                self.ui.listWidget_Pontos.addItem(str([i.x,i.y]))

    def updatecanvas(self):
        if str(self.ui.comboBox_Poligono.currentText()) =="B-Splines" :
                    
                if self.bspline > 3 :

                    #print("iniciou")
                    self.bspline = 0
                    self.poliAux.pontos = []
                    #print(len(self.bsplinespontos))
                    for i  in range(3,len(self.bsplinespontos)):
                        
                        
                        test = b_spline([[self.bsplinespontos[i-3].x,self.bsplinespontos[i-3].y],[self.bsplinespontos[i-2].x,self.bsplinespontos[i-2].y],[self.bsplinespontos[i-1].x,self.bsplinespontos[i-1].y],[self.bsplinespontos[i].x,self.bsplinespontos[i].y]])
                        for j in test:
                            
                            self.poliAux.pontos.append(Ponto(j[0],j[1]))

                    #print("acabou")
                    self.bsplinespontos = []    
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.comboBox_Poligono.currentText())
                   
                    self.ultimoid += 1
                    
                    self.display.poligonos.append( copy.copy(self.poliAux))
        elif  str(self.ui.comboBox_Poligono.currentText()) =="B-Splines-Forward":
                    
                if self.bspline > 3 :

                    #print("iniciou")
                    self.bspline = 0
                    self.poliAux.pontos = []
                    
                    for i  in range(3,len(self.bsplinespontos)):
                        
                        t = 0
        
        
                        #while (t <= 1):
                        #for k in np.linspace(0,1,100):
                        test = b_spline_forward([[self.bsplinespontos[i-3].x,self.bsplinespontos[i-3].y],[self.bsplinespontos[i-2].x,self.bsplinespontos[i-2].y],[self.bsplinespontos[i-1].x,self.bsplinespontos[i-1].y],[self.bsplinespontos[i].x,self.bsplinespontos[i].y]],0.01)
                        #t = t+0.01
                        for i  in test:
                            self.poliAux.pontos.append(Ponto(i[0],i[1]))

                    #print("acabou")
                    self.bsplinespontos = []    
                    self.poliAux.Id = self.ultimoid
                    
                    self.poliAux.tipo =  str(self.ui.comboBox_Poligono.currentText())
                   
                    self.ultimoid += 1
                    
                    self.display.poligonos.append( copy.copy(self.poliAux))
                
        
        self.update()

    """ --------------------------------------------------------"""

     #Metodos de conversões ViewPort para Mundo.
    
    """ --------------------------------------------------------"""

        
        
    def XVp2w(self,x):
                return  (( x - self.viewport.xmin)/(self.viewport.xmax- self.viewport.xmin))*(self.mundo.xmax - self.mundo.xmin) + self.mundo.xmin;
    
        
    def YVp2w(self,y):
        
        return  (1-(y - self.viewport.ymin)/(self.viewport.ymax- self.viewport.ymin))*(self.mundo.ymax - self.mundo.ymin) + self.mundo.ymin;






