# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(896, 647)
        Form.setMouseTracking(False)
        self.frame_botoes = QtWidgets.QFrame(Form)
        self.frame_botoes.setGeometry(QtCore.QRect(9, 10, 161, 611))
        self.frame_botoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_botoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_botoes.setObjectName("frame_botoes")
        self.pushButton_subir = QtWidgets.QPushButton(self.frame_botoes)
        self.pushButton_subir.setGeometry(QtCore.QRect(40, 110, 51, 21))
        self.pushButton_subir.setObjectName("pushButton_subir")
        self.pushButton_descer = QtWidgets.QPushButton(self.frame_botoes)
        self.pushButton_descer.setGeometry(QtCore.QRect(40, 150, 51, 21))
        self.pushButton_descer.setObjectName("pushButton_descer")
        self.pushButton_esquerda = QtWidgets.QPushButton(self.frame_botoes)
        self.pushButton_esquerda.setGeometry(QtCore.QRect(10, 130, 61, 21))
        self.pushButton_esquerda.setObjectName("pushButton_esquerda")
        self.pushButton_direita = QtWidgets.QPushButton(self.frame_botoes)
        self.pushButton_direita.setGeometry(QtCore.QRect(70, 130, 51, 21))
        self.pushButton_direita.setObjectName("pushButton_direita")
        self.label_zoom = QtWidgets.QLabel(self.frame_botoes)
        self.label_zoom.setGeometry(QtCore.QRect(10, 40, 31, 17))
        self.label_zoom.setObjectName("label_zoom")
        self.pushButton_zoommais = QtWidgets.QPushButton(self.frame_botoes)
        self.pushButton_zoommais.setGeometry(QtCore.QRect(50, 30, 20, 27))
        self.pushButton_zoommais.setObjectName("pushButton_zoommais")
        self.pushButton_zoommenos = QtWidgets.QPushButton(self.frame_botoes)
        self.pushButton_zoommenos.setGeometry(QtCore.QRect(70, 30, 21, 27))
        self.pushButton_zoommenos.setObjectName("pushButton_zoommenos")
        self.frame = QtWidgets.QFrame(self.frame_botoes)
        self.frame.setGeometry(QtCore.QRect(10, 200, 141, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_Poligono = QtWidgets.QLabel(self.frame)
        self.label_Poligono.setGeometry(QtCore.QRect(40, 0, 54, 17))
        self.label_Poligono.setObjectName("label_Poligono")
        self.comboBox_Poligono = QtWidgets.QComboBox(self.frame)
        self.comboBox_Poligono.setGeometry(QtCore.QRect(20, 30, 101, 27))
        self.comboBox_Poligono.setObjectName("comboBox_Poligono")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.comboBox_Poligono.addItem("")
        self.pushButton_desenhar = QtWidgets.QPushButton(self.frame)
        self.pushButton_desenhar.setGeometry(QtCore.QRect(30, 110, 85, 27))
        self.pushButton_desenhar.setObjectName("pushButton_desenhar")
        self.pushButton_Limpar_canvas = QtWidgets.QPushButton(self.frame)
        self.pushButton_Limpar_canvas.setGeometry(QtCore.QRect(30, 80, 85, 27))
        self.pushButton_Limpar_canvas.setObjectName("pushButton_Limpar_canvas")
        self.listWidget_Poligonos = QtWidgets.QListWidget(self.frame_botoes)
        self.listWidget_Poligonos.setGeometry(QtCore.QRect(10, 380, 131, 91))
        self.listWidget_Poligonos.setObjectName("listWidget_Poligonos")
        self.listWidget_Pontos = QtWidgets.QListWidget(self.frame_botoes)
        self.listWidget_Pontos.setGeometry(QtCore.QRect(10, 490, 131, 91))
        self.listWidget_Pontos.setObjectName("listWidget_Pontos")
        self.label_textpoligonos = QtWidgets.QLabel(self.frame_botoes)
        self.label_textpoligonos.setGeometry(QtCore.QRect(10, 360, 61, 17))
        self.label_textpoligonos.setObjectName("label_textpoligonos")
        self.label_textPontos = QtWidgets.QLabel(self.frame_botoes)
        self.label_textPontos.setGeometry(QtCore.QRect(10, 470, 61, 17))
        self.label_textPontos.setObjectName("label_textPontos")
        self.spinBox_zoom = QtWidgets.QSpinBox(self.frame_botoes)
        self.spinBox_zoom.setGeometry(QtCore.QRect(104, 30, 51, 27))
        self.spinBox_zoom.setMaximum(1000)
        self.spinBox_zoom.setProperty("value", 10)
        self.spinBox_zoom.setObjectName("spinBox_zoom")
        self.comboBox_zoom = QtWidgets.QComboBox(self.frame_botoes)
        self.comboBox_zoom.setGeometry(QtCore.QRect(30, 70, 91, 27))
        self.comboBox_zoom.setObjectName("comboBox_zoom")
        self.comboBox_zoom.addItem("")
        self.comboBox_zoom.addItem("")
        self.label_viewport = QtWidgets.QLabel(Form)
        self.label_viewport.setGeometry(QtCore.QRect(180, 50, 54, 17))
        self.label_viewport.setObjectName("label_viewport")
        self.label_xyview = QtWidgets.QLabel(Form)
        self.label_xyview.setGeometry(QtCore.QRect(230, 580, 121, 17))
        self.label_xyview.setObjectName("label_xyview")
        self.label_xymundo = QtWidgets.QLabel(Form)
        self.label_xymundo.setGeometry(QtCore.QRect(600, 580, 141, 20))
        self.label_xymundo.setObjectName("label_xymundo")
        self.label_viewportlabel = QtWidgets.QLabel(Form)
        self.label_viewportlabel.setGeometry(QtCore.QRect(210, 580, 16, 16))
        self.label_viewportlabel.setObjectName("label_viewportlabel")
        self.label_mundolabel = QtWidgets.QLabel(Form)
        self.label_mundolabel.setGeometry(QtCore.QRect(560, 580, 41, 20))
        self.label_mundolabel.setObjectName("label_mundolabel")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(180, 70, 500, 500))
        self.widget.setObjectName("widget")
        self.tabWidget_cordenadas = QtWidgets.QTabWidget(Form)
        self.tabWidget_cordenadas.setGeometry(QtCore.QRect(690, 10, 191, 611))
        self.tabWidget_cordenadas.setStyleSheet("")
        self.tabWidget_cordenadas.setObjectName("tabWidget_cordenadas")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.doubleSpinBox_mxmin = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_mxmin.setGeometry(QtCore.QRect(90, 20, 62, 27))
        self.doubleSpinBox_mxmin.setMinimum(-1000000000.0)
        self.doubleSpinBox_mxmin.setMaximum(100000000000.0)
        self.doubleSpinBox_mxmin.setObjectName("doubleSpinBox_mxmin")
        self.label_mxmin = QtWidgets.QLabel(self.tab)
        self.label_mxmin.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.label_mxmin.setObjectName("label_mxmin")
        self.doubleSpinBox_mxmax = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_mxmax.setGeometry(QtCore.QRect(90, 50, 62, 27))
        self.doubleSpinBox_mxmax.setDecimals(2)
        self.doubleSpinBox_mxmax.setMinimum(-1e+17)
        self.doubleSpinBox_mxmax.setMaximum(1000000000000.0)
        self.doubleSpinBox_mxmax.setObjectName("doubleSpinBox_mxmax")
        self.label_mxmin_2 = QtWidgets.QLabel(self.tab)
        self.label_mxmin_2.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.label_mxmin_2.setObjectName("label_mxmin_2")
        self.doubleSpinBox_mymin = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_mymin.setGeometry(QtCore.QRect(90, 80, 62, 27))
        self.doubleSpinBox_mymin.setMinimum(-1000000000000.0)
        self.doubleSpinBox_mymin.setMaximum(10000000000.0)
        self.doubleSpinBox_mymin.setObjectName("doubleSpinBox_mymin")
        self.label_mxmin_3 = QtWidgets.QLabel(self.tab)
        self.label_mxmin_3.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_mxmin_3.setObjectName("label_mxmin_3")
        self.doubleSpinBox_mymax = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBox_mymax.setGeometry(QtCore.QRect(90, 110, 62, 27))
        self.doubleSpinBox_mymax.setMinimum(-100000000.0)
        self.doubleSpinBox_mymax.setMaximum(1000000000.0)
        self.doubleSpinBox_mymax.setObjectName("doubleSpinBox_mymax")
        self.label_mxmin_4 = QtWidgets.QLabel(self.tab)
        self.label_mxmin_4.setGeometry(QtCore.QRect(10, 110, 81, 21))
        self.label_mxmin_4.setObjectName("label_mxmin_4")
        self.pushButton_SetMundo = QtWidgets.QPushButton(self.tab)
        self.pushButton_SetMundo.setGeometry(QtCore.QRect(50, 150, 85, 27))
        self.pushButton_SetMundo.setObjectName("pushButton_SetMundo")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 199, 171, 191))
        self.tabWidget_2.setAccessibleName("")
        self.tabWidget_2.setStyleSheet("")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_translacao = QtWidgets.QWidget()
        self.tabWidget_translacao.setObjectName("tabWidget_translacao")
        self.doubleSpinBox_dx = QtWidgets.QDoubleSpinBox(self.tabWidget_translacao)
        self.doubleSpinBox_dx.setGeometry(QtCore.QRect(60, 10, 62, 27))
        self.doubleSpinBox_dx.setMinimum(-1000000.0)
        self.doubleSpinBox_dx.setMaximum(1000000000.0)
        self.doubleSpinBox_dx.setObjectName("doubleSpinBox_dx")
        self.label_dx = QtWidgets.QLabel(self.tabWidget_translacao)
        self.label_dx.setGeometry(QtCore.QRect(30, 10, 31, 21))
        self.label_dx.setObjectName("label_dx")
        self.label_dy = QtWidgets.QLabel(self.tabWidget_translacao)
        self.label_dy.setGeometry(QtCore.QRect(30, 40, 31, 21))
        self.label_dy.setObjectName("label_dy")
        self.doubleSpinBox_dy = QtWidgets.QDoubleSpinBox(self.tabWidget_translacao)
        self.doubleSpinBox_dy.setGeometry(QtCore.QRect(60, 40, 62, 27))
        self.doubleSpinBox_dy.setMinimum(-100000000.0)
        self.doubleSpinBox_dy.setMaximum(1000000000.0)
        self.doubleSpinBox_dy.setObjectName("doubleSpinBox_dy")
        self.pushButton_translate = QtWidgets.QPushButton(self.tabWidget_translacao)
        self.pushButton_translate.setGeometry(QtCore.QRect(40, 110, 85, 27))
        self.pushButton_translate.setObjectName("pushButton_translate")
        self.label_dz = QtWidgets.QLabel(self.tabWidget_translacao)
        self.label_dz.setGeometry(QtCore.QRect(30, 70, 31, 21))
        self.label_dz.setObjectName("label_dz")
        self.doubleSpinBox_dz = QtWidgets.QDoubleSpinBox(self.tabWidget_translacao)
        self.doubleSpinBox_dz.setGeometry(QtCore.QRect(60, 70, 62, 27))
        self.doubleSpinBox_dz.setMinimum(-100000000.0)
        self.doubleSpinBox_dz.setMaximum(1000000000.0)
        self.doubleSpinBox_dz.setObjectName("doubleSpinBox_dz")
        self.tabWidget_2.addTab(self.tabWidget_translacao, "")
        self.tabWidget_2Page2 = QtWidgets.QWidget()
        self.tabWidget_2Page2.setObjectName("tabWidget_2Page2")
        self.pushButton_scale = QtWidgets.QPushButton(self.tabWidget_2Page2)
        self.pushButton_scale.setGeometry(QtCore.QRect(40, 90, 85, 27))
        self.pushButton_scale.setObjectName("pushButton_scale")
        self.label_sy = QtWidgets.QLabel(self.tabWidget_2Page2)
        self.label_sy.setGeometry(QtCore.QRect(30, 30, 31, 21))
        self.label_sy.setObjectName("label_sy")
        self.label_sx = QtWidgets.QLabel(self.tabWidget_2Page2)
        self.label_sx.setGeometry(QtCore.QRect(30, 0, 31, 20))
        self.label_sx.setObjectName("label_sx")
        self.doubleSpinBox_sx = QtWidgets.QDoubleSpinBox(self.tabWidget_2Page2)
        self.doubleSpinBox_sx.setGeometry(QtCore.QRect(60, 0, 62, 26))
        self.doubleSpinBox_sx.setMinimum(-1000000000.0)
        self.doubleSpinBox_sx.setMaximum(1000000000.0)
        self.doubleSpinBox_sx.setProperty("value", 1.0)
        self.doubleSpinBox_sx.setObjectName("doubleSpinBox_sx")
        self.doubleSpinBox_sy = QtWidgets.QDoubleSpinBox(self.tabWidget_2Page2)
        self.doubleSpinBox_sy.setGeometry(QtCore.QRect(60, 30, 62, 27))
        self.doubleSpinBox_sy.setMinimum(-100000000.0)
        self.doubleSpinBox_sy.setMaximum(1000000000.0)
        self.doubleSpinBox_sy.setProperty("value", 1.0)
        self.doubleSpinBox_sy.setObjectName("doubleSpinBox_sy")
        self.pushButton_scale_homo = QtWidgets.QPushButton(self.tabWidget_2Page2)
        self.pushButton_scale_homo.setGeometry(QtCore.QRect(30, 120, 111, 27))
        self.pushButton_scale_homo.setObjectName("pushButton_scale_homo")
        self.doubleSpinBox_sz = QtWidgets.QDoubleSpinBox(self.tabWidget_2Page2)
        self.doubleSpinBox_sz.setGeometry(QtCore.QRect(60, 60, 62, 27))
        self.doubleSpinBox_sz.setMinimum(-100000000.0)
        self.doubleSpinBox_sz.setMaximum(1000000000.0)
        self.doubleSpinBox_sz.setProperty("value", 1.0)
        self.doubleSpinBox_sz.setObjectName("doubleSpinBox_sz")
        self.label_sz = QtWidgets.QLabel(self.tabWidget_2Page2)
        self.label_sz.setGeometry(QtCore.QRect(30, 60, 31, 21))
        self.label_sz.setObjectName("label_sz")
        self.tabWidget_2.addTab(self.tabWidget_2Page2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_Rotacionar = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Rotacionar.setGeometry(QtCore.QRect(40, 90, 85, 27))
        self.pushButton_Rotacionar.setObjectName("pushButton_Rotacionar")
        self.doubleSpinBox_anguloy = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_anguloy.setGeometry(QtCore.QRect(80, 30, 62, 27))
        self.doubleSpinBox_anguloy.setMinimum(-1000000000.0)
        self.doubleSpinBox_anguloy.setMaximum(1000000000.0)
        self.doubleSpinBox_anguloy.setObjectName("doubleSpinBox_anguloy")
        self.label_anguloy = QtWidgets.QLabel(self.tab_3)
        self.label_anguloy.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.label_anguloy.setObjectName("label_anguloy")
        self.pushButton_Rotacionar_homo = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_Rotacionar_homo.setGeometry(QtCore.QRect(30, 120, 111, 27))
        self.pushButton_Rotacionar_homo.setObjectName("pushButton_Rotacionar_homo")
        self.label_angulo = QtWidgets.QLabel(self.tab_3)
        self.label_angulo.setGeometry(QtCore.QRect(20, 0, 61, 21))
        self.label_angulo.setObjectName("label_angulo")
        self.doubleSpinBox_angulo = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_angulo.setGeometry(QtCore.QRect(80, 0, 62, 27))
        self.doubleSpinBox_angulo.setMinimum(-1000000000.0)
        self.doubleSpinBox_angulo.setMaximum(1000000000.0)
        self.doubleSpinBox_angulo.setObjectName("doubleSpinBox_angulo")
        self.label_anguloz = QtWidgets.QLabel(self.tab_3)
        self.label_anguloz.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.label_anguloz.setObjectName("label_anguloz")
        self.doubleSpinBox_anguloz = QtWidgets.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_anguloz.setGeometry(QtCore.QRect(80, 60, 62, 27))
        self.doubleSpinBox_anguloz.setMinimum(-1000000000.0)
        self.doubleSpinBox_anguloz.setMaximum(1000000000.0)
        self.doubleSpinBox_anguloz.setObjectName("doubleSpinBox_anguloz")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.radioButton_eixox = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_eixox.setGeometry(QtCore.QRect(30, 40, 100, 22))
        self.radioButton_eixox.setObjectName("radioButton_eixox")
        self.radioButton_eixoy = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_eixoy.setGeometry(QtCore.QRect(30, 70, 100, 22))
        self.radioButton_eixoy.setObjectName("radioButton_eixoy")
        self.pushButton_Refletir = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_Refletir.setGeometry(QtCore.QRect(40, 100, 85, 27))
        self.pushButton_Refletir.setObjectName("pushButton_Refletir")
        self.radioButton_origem = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_origem.setGeometry(QtCore.QRect(30, 10, 100, 22))
        self.radioButton_origem.setObjectName("radioButton_origem")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.PushButton_Clipping = QtWidgets.QPushButton(self.tab)
        self.PushButton_Clipping.setGeometry(QtCore.QRect(50, 400, 85, 27))
        self.PushButton_Clipping.setObjectName("PushButton_Clipping")
        self.label_textpoligonos_2 = QtWidgets.QLabel(self.tab)
        self.label_textpoligonos_2.setGeometry(QtCore.QRect(60, 450, 101, 17))
        self.label_textpoligonos_2.setObjectName("label_textpoligonos_2")
        self.listWidget_Poligonos_Tipo = QtWidgets.QListWidget(self.tab)
        self.listWidget_Poligonos_Tipo.setGeometry(QtCore.QRect(30, 470, 131, 91))
        self.listWidget_Poligonos_Tipo.setObjectName("listWidget_Poligonos_Tipo")
        self.tabWidget_cordenadas.addTab(self.tab, "")
        self.label_mensagemdivisaoporzero = QtWidgets.QLabel(Form)
        self.label_mensagemdivisaoporzero.setGeometry(QtCore.QRect(240, 20, 321, 20))
        self.label_mensagemdivisaoporzero.setText("")
        self.label_mensagemdivisaoporzero.setObjectName("label_mensagemdivisaoporzero")
        self.pushButton_3D = QtWidgets.QPushButton(Form)
        self.pushButton_3D.setGeometry(QtCore.QRect(400, 30, 85, 27))
        self.pushButton_3D.setObjectName("pushButton_3D")
        self.label_viewport.raise_()
        self.frame_botoes.raise_()
        self.label_xyview.raise_()
        self.label_xymundo.raise_()
        self.label_viewportlabel.raise_()
        self.label_mundolabel.raise_()
        self.widget.raise_()
        self.tabWidget_cordenadas.raise_()
        self.label_mensagemdivisaoporzero.raise_()
        self.pushButton_3D.raise_()

        self.retranslateUi(Form)
        self.tabWidget_cordenadas.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Computação Gráfica"))
        self.pushButton_subir.setText(_translate("Form", "Subir"))
        self.pushButton_descer.setText(_translate("Form", "Descer"))
        self.pushButton_esquerda.setText(_translate("Form", "Esquerda"))
        self.pushButton_direita.setText(_translate("Form", "Direita"))
        self.label_zoom.setText(_translate("Form", "Zoom:"))
        self.pushButton_zoommais.setText(_translate("Form", "+"))
        self.pushButton_zoommenos.setText(_translate("Form", "-"))
        self.label_Poligono.setText(_translate("Form", "Polígono"))
        self.comboBox_Poligono.setItemText(0, _translate("Form", "LineTo"))
        self.comboBox_Poligono.setItemText(1, _translate("Form", "DDA"))
        self.comboBox_Poligono.setItemText(2, _translate("Form", "Bresenham"))
        self.comboBox_Poligono.setItemText(3, _translate("Form", "Circunferência"))
        self.comboBox_Poligono.setItemText(4, _translate("Form", "Poligono"))
        self.comboBox_Poligono.setItemText(5, _translate("Form", "deCasteljau"))
        self.comboBox_Poligono.setItemText(6, _translate("Form", "Hermite"))
        self.comboBox_Poligono.setItemText(7, _translate("Form", "Bezier"))
        self.comboBox_Poligono.setItemText(8, _translate("Form", "B-Splines"))
        self.comboBox_Poligono.setItemText(9, _translate("Form", "B-Splines-Forward"))
        self.pushButton_desenhar.setText(_translate("Form", "Desenhar"))
        self.pushButton_Limpar_canvas.setText(_translate("Form", "Limpar"))
        self.label_textpoligonos.setText(_translate("Form", "Poligonos"))
        self.label_textPontos.setText(_translate("Form", "Pontos"))
        self.comboBox_zoom.setItemText(0, _translate("Form", "Valor"))
        self.comboBox_zoom.setItemText(1, _translate("Form", "Porcentagem"))
        self.label_viewport.setText(_translate("Form", "ViewPort"))
        self.label_xyview.setText(_translate("Form", "xy view"))
        self.label_xymundo.setText(_translate("Form", "xy mundo"))
        self.label_viewportlabel.setText(_translate("Form", "VP:"))
        self.label_mundolabel.setText(_translate("Form", "World:"))
        self.tabWidget_cordenadas.setWhatsThis(_translate("Form", "<html><head/><body><p>tes</p></body></html>"))
        self.label_mxmin.setText(_translate("Form", "Mundo Xmin"))
        self.label_mxmin_2.setText(_translate("Form", "Mundo Xmax"))
        self.label_mxmin_3.setText(_translate("Form", "Mundo Ymin"))
        self.label_mxmin_4.setText(_translate("Form", "Mundo Ymax"))
        self.pushButton_SetMundo.setText(_translate("Form", "Atualizar"))
        self.tabWidget_2.setToolTip(_translate("Form", "<html><head/><body><p>teste</p></body></html>"))
        self.label_dx.setText(_translate("Form", "DX:"))
        self.label_dy.setText(_translate("Form", "DY:"))
        self.pushButton_translate.setText(_translate("Form", "Translate"))
        self.label_dz.setText(_translate("Form", "DZ:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_translacao), _translate("Form", "Translação"))
        self.pushButton_scale.setText(_translate("Form", "Scale"))
        self.label_sy.setText(_translate("Form", "SY:"))
        self.label_sx.setText(_translate("Form", "SX:"))
        self.pushButton_scale_homo.setText(_translate("Form", "Scale Homogenio"))
        self.label_sz.setText(_translate("Form", "SZ:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tabWidget_2Page2), _translate("Form", "Escalonamento"))
        self.pushButton_Rotacionar.setText(_translate("Form", "Rotacionar"))
        self.label_anguloy.setText(_translate("Form", "Angulo y:"))
        self.pushButton_Rotacionar_homo.setText(_translate("Form", "Rotacionar Homo"))
        self.label_angulo.setText(_translate("Form", "Angulo x:"))
        self.label_anguloz.setText(_translate("Form", "Angulo z:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("Form", "Rotação"))
        self.radioButton_eixox.setText(_translate("Form", "Eixo X"))
        self.radioButton_eixoy.setText(_translate("Form", "Eixo Y"))
        self.pushButton_Refletir.setText(_translate("Form", "Refletir"))
        self.radioButton_origem.setText(_translate("Form", "x e y"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Form", "Reflexão"))
        self.PushButton_Clipping.setText(_translate("Form", "Clipping"))
        self.label_textpoligonos_2.setText(_translate("Form", "Alterar Tipo"))
        self.tabWidget_cordenadas.setTabText(self.tabWidget_cordenadas.indexOf(self.tab), _translate("Form", "Cordenadas Change"))
        self.pushButton_3D.setText(_translate("Form", "3D-Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

