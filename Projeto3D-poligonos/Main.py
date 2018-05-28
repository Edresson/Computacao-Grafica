import sys

####Imports Clases ####
from Modulos.Principal import *



app = qt.QtWidgets.QApplication(sys.argv)
Form = qt.QtWidgets.QWidget()
ui = qt.Ui_Form()
ui.setupUi(Form)



Ca = Principal(Form,ui)#Instanciando um objeto da Classe Principals
ui.pushButton_3D.clicked.connect(Ca.browser_files)  # browser
### Botoes Clicks 
ui.pushButton_desenhar.clicked.connect(Ca.updatecanvas)
ui.pushButton_Limpar_canvas.clicked.connect(Ca.Clear)
ui.pushButton_zoommais.clicked.connect(Ca.ZoomMais)
ui.pushButton_zoommenos.clicked.connect(Ca.ZoomMenos)
ui.pushButton_descer.clicked.connect(Ca.Descer)
ui.pushButton_esquerda.clicked.connect(Ca.Esquerda)
ui.pushButton_direita.clicked.connect(Ca.Direita)
ui.pushButton_subir.clicked.connect(Ca.Subir)
ui.pushButton_SetMundo.clicked.connect(Ca.Set_Mundo_pinBox)
ui.listWidget_Poligonos.currentItemChanged.connect(Ca.updatelistbox_pontos)
ui.pushButton_translate.clicked.connect(Ca.Translater)
ui.pushButton_scale.clicked.connect(Ca.Escale)
ui.pushButton_scale_homo.clicked.connect(Ca.EscaleHomo)
ui.pushButton_Rotacionar_homo.clicked.connect(Ca.RotacaoHomo)
ui.pushButton_Rotacionar.clicked.connect(Ca.Rotacao)
ui.pushButton_Refletir.clicked.connect(Ca.Reflexao)
ui.PushButton_Clipping.clicked.connect(Ca.Clipping)
ui.listWidget_Poligonos_Tipo.currentItemChanged.connect(Ca.Press_ListPoligono_Tipo)
Form.show()
sys.exit(app.exec_())


    
