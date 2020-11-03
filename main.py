from ventana import *
from calendario import *
from venSalir import *
import sys, var, events, clients, datetime


class DialogSalir(object):
    pass


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_venPrincipal()
        var.ui.setupUi(self)
        '''
        conexion de eventos con los objetos
        '''
        var.rbtsex = (var.ui.rbtFem, var.ui.rbtMasc)
        var.chkpago=(var.ui.chkEfect,var.ui.chkTar,var.ui.chkTrans)
        var.avisosalir = DialogSalir()
        var.glgcalendar = DialogCalendar()
        '''
        conexion de eventos con los objetos
        estamos conectando el codigo con la interfaz grafica
        '''
        QtWidgets.QAction(self).triggered.connect
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.editDni.editingFinished.connect(clients.Clientes.validoDni)
        var.ui.btnCalendar.clicked.connect(clients.Clientes.abrirCalendar)
        for i in var.rbtsex:
            i.toggled.connect(clients.Clientes.selSexo)
        for i in var.chkpago:
            i.stateChanged.connect(clients.Clientes.selPago)
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)

        '''
        llamada a modulos iniciales
        '''
        events.Eventos.cargarProv()

class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.avisosalir = Ui_venSalir()
        var.avisosalir.setupUi(self)
        var.dialog.btnBoxSalir.button(QtWidgets.QDialogButtonBox.Yes).clicked.connect(events.Eventos.Salir)
        var.dialog.btnBoxSalir.button(QtWidgets.QDialogButtonBox.No).clicked.connect(events.Eventos.Salir)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar,self).__init__()
        var.glgcalendar = Ui_Calender()
        var.glgcalendar.setupUi(self)
        mesactual= datetime.now().month
        anoactual= datetime.now().year
        var.glgcalendar.Calender.setSelectedDate((QtCore.QDate(anoactual,mesactual,1)))
        var.glgcalendar.Calender.clicked.connect(clients.Clientes.cargarFecha)

    def closeEvent(self,event):
        events.Eventos.Salir()

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())