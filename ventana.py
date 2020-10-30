# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_venPrincipal(object):
    def setupUi(self, venPrincipal):
        venPrincipal.setObjectName("venPrincipal")
        venPrincipal.resize(651, 444)
        self.centralwidget = QtWidgets.QWidget(venPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.lblXexCli = QtWidgets.QLabel(self.centralwidget)
        self.lblXexCli.setGeometry(QtCore.QRect(250, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblXexCli.setFont(font)
        self.lblXexCli.setStyleSheet("background-color: rgb(179, 254, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.46, y1:0.0343636, x2:0.4595, y2:0.835, stop:0 rgba(0, 223, 185, 255), stop:1 rgba(255, 255, 255, 255));")
        self.lblXexCli.setAlignment(QtCore.Qt.AlignCenter)
        self.lblXexCli.setObjectName("lblXexCli")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 40, 651, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lblDNI = QtWidgets.QLabel(self.centralwidget)
        self.lblDNI.setGeometry(QtCore.QRect(40, 70, 41, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 180, 651, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.editDni = QtWidgets.QLineEdit(self.centralwidget)
        self.editDni.setGeometry(QtCore.QRect(90, 70, 141, 20))
        self.editDni.setObjectName("editDni")
        self.lblApel = QtWidgets.QLabel(self.centralwidget)
        self.lblApel.setGeometry(QtCore.QRect(30, 100, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.editApel = QtWidgets.QLineEdit(self.centralwidget)
        self.editApel.setGeometry(QtCore.QRect(90, 100, 251, 20))
        self.editApel.setObjectName("editApel")
        self.lblNome = QtWidgets.QLabel(self.centralwidget)
        self.lblNome.setGeometry(QtCore.QRect(360, 100, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.editNome = QtWidgets.QLineEdit(self.centralwidget)
        self.editNome.setGeometry(QtCore.QRect(420, 100, 201, 20))
        self.editNome.setObjectName("editNome")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(230, 200, 71, 21))
        self.btnAceptar.setObjectName("btnAceptar")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(330, 200, 71, 21))
        self.btnSalir.setObjectName("btnSalir")
        self.lblValidar = QtWidgets.QLabel(self.centralwidget)
        self.lblValidar.setGeometry(QtCore.QRect(250, 60, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.lblValidar.setFont(font)
        self.lblValidar.setText("")
        self.lblValidar.setObjectName("lblValidar")
        self.rbtFem = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtFem.setGeometry(QtCore.QRect(90, 160, 82, 17))
        self.rbtFem.setObjectName("rbtFem")
        self.lblSex = QtWidgets.QLabel(self.centralwidget)
        self.lblSex.setGeometry(QtCore.QRect(40, 160, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblSex.setFont(font)
        self.lblSex.setObjectName("lblSex")
        self.rbtMasc = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtMasc.setGeometry(QtCore.QRect(170, 160, 82, 17))
        self.rbtMasc.setObjectName("rbtMasc")
        self.lblPago = QtWidgets.QLabel(self.centralwidget)
        self.lblPago.setGeometry(QtCore.QRect(280, 160, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblPago.setFont(font)
        self.lblPago.setObjectName("lblPago")
        self.chkEfect = QtWidgets.QCheckBox(self.centralwidget)
        self.chkEfect.setGeometry(QtCore.QRect(400, 160, 70, 17))
        self.chkEfect.setObjectName("chkEfect")
        self.chkTar = QtWidgets.QCheckBox(self.centralwidget)
        self.chkTar.setGeometry(QtCore.QRect(480, 160, 70, 17))
        self.chkTar.setObjectName("chkTar")
        self.chkTrans = QtWidgets.QCheckBox(self.centralwidget)
        self.chkTrans.setGeometry(QtCore.QRect(560, 160, 91, 17))
        self.chkTrans.setObjectName("chkTrans")
        self.lblDir = QtWidgets.QLabel(self.centralwidget)
        self.lblDir.setGeometry(QtCore.QRect(30, 130, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.editApel_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.editApel_2.setGeometry(QtCore.QRect(90, 130, 291, 20))
        self.editApel_2.setObjectName("editApel_2")
        self.lblProv = QtWidgets.QLabel(self.centralwidget)
        self.lblProv.setGeometry(QtCore.QRect(390, 130, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblProv.setFont(font)
        self.lblProv.setObjectName("lblProv")
        self.cmbProv = QtWidgets.QComboBox(self.centralwidget)
        self.cmbProv.setGeometry(QtCore.QRect(460, 130, 161, 22))
        self.cmbProv.setObjectName("cmbProv")
        venPrincipal.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(venPrincipal)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuArchivo = QtWidgets.QMenu(self.menuBar)
        self.menuArchivo.setObjectName("menuArchivo")
        venPrincipal.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(venPrincipal)
        self.statusbar.setObjectName("statusbar")
        venPrincipal.setStatusBar(self.statusbar)
        self.actionSalir = QtWidgets.QAction(venPrincipal)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menuBar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(venPrincipal)
        QtCore.QMetaObject.connectSlotsByName(venPrincipal)

    def retranslateUi(self, venPrincipal):
        _translate = QtCore.QCoreApplication.translate
        venPrincipal.setWindowTitle(_translate("venPrincipal", "Proyecto Uno"))
        self.lblXexCli.setText(_translate("venPrincipal", "XESTIÓN CLIENTES"))
        self.lblDNI.setText(_translate("venPrincipal", "DNI: "))
        self.lblApel.setText(_translate("venPrincipal", "Apellidos: "))
        self.lblNome.setText(_translate("venPrincipal", "Nombre: "))
        self.btnAceptar.setText(_translate("venPrincipal", "Aceptar"))
        self.btnSalir.setText(_translate("venPrincipal", "Salir"))
        self.rbtFem.setText(_translate("venPrincipal", "Femenino"))
        self.lblSex.setText(_translate("venPrincipal", "Sexo:"))
        self.rbtMasc.setText(_translate("venPrincipal", "Masculino"))
        self.lblPago.setText(_translate("venPrincipal", "Metodos de pago:"))
        self.chkEfect.setText(_translate("venPrincipal", "Efectivo"))
        self.chkTar.setText(_translate("venPrincipal", "Tarjeta"))
        self.chkTrans.setText(_translate("venPrincipal", "Transferencia"))
        self.lblDir.setText(_translate("venPrincipal", "Direccion:"))
        self.lblProv.setText(_translate("venPrincipal", "Provincia:"))
        self.menuArchivo.setTitle(_translate("venPrincipal", "Archivo"))
        self.actionSalir.setText(_translate("venPrincipal", "Salir"))
        self.actionSalir.setShortcut(_translate("venPrincipal", "Alt+S"))
