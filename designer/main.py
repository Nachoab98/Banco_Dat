from PyQt6 import uic  #permite convertir el designer a python
from PyQt6.QtWidgets import QMessageBox
from data.pais import paisData
from data.transferencia import TransferenciaData
from designer import registrarFichaje
from model.movimiento import Transferencia

class MainFichaje():
    def __init__(self):
        self.main = uic.loadUi('designer/main.ui')
        self.iniciarGUI()
        self.main.showMaximized()

    def iniciarGUI(self):
        self.main.btnRegistrar_Fichajes.triggered.connect(self.abrirRegistrarFichaje) #se ejecuta solo cuando se interactua con el boton
        self.main.btnReportar_fichaje.triggered.connect(self.abrirReportarFichaje) #se ejecuta solo cuando se interactua con el boton
        self.registro = uic.loadUi('designer/registrarFichaje.ui')
        self.reporte = uic.loadUi('designer/reportarFichaje.ui')

    def abrirRegistrarFichaje(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransferencia) #se ejecuta solo cuando se interactua con el boton
        self.registro.show()
    
    def abrirReportarFichaje(self):
        self.reporte.btnAceptar.clicked.connect(self.registrarTransferencia) #se ejecuta solo cuando se interactua con el boton
        self.reporte.show()
        self.llenarComboPaises()

    ## Transferencias ##
    def registrarTransferencia(self):   
        if self.registro.boxFichajes.currentText() == "--- Seleccione ---":
            mBox= QMessageBox()
            mBox.setText("Seleccione un tipo de fichaje")
            mBox.exec()
            self.registro.boxFichajes.setFocus()


        elif self.registro.txtClub.text() == "":
            mBox= QMessageBox()
            mBox.setText("Ingrese el club")
            mBox.exec()
            self.registro.txtClub.setFocus()


        elif self.registro.txtCuota.text() == "":
            mBox= QMessageBox()
            mBox.setText("Ingrese la/s cuota/s")
            mBox.exec()
            self.registro.txtCuota.setFocus()

        
        elif not self.registro.txtMonto.text().isnumeric():
            mBox= QMessageBox()
            mBox.setText("Ingrese el monto")
            mBox.exec()
            self.registro.txtMonto.setText("0")
            self.registro.txtMonto.setFocus()
        else:
            transferencia = Transferencia(
                tipo= self.registro.boxFichajes.currentText(),
                clubOrigen= self.registro.txtClub.text(),
                monto= float(self.registro.txtMonto.text()),
                cuota= int(self.registro.txtCuota.text()),
                internacional= self.registro.checkInternacional.isChecked()
            )
            
        objData = TransferenciaData()
        mBox= QMessageBox()
        if objData.registrar(info = transferencia):
            mBox.setText("Transferencia exitosa")
            self.limpiarCamposTransferencia()
        else:
            mBox.setText("Error al realizar la transferencia")
        mBox.exec()

    def limpiarCamposTransferencia(self):
        self.registro.boxFichajes.setCurrentIndex(0)
        self.registro.txtClub.setText("")
        self.registro.txtMonto.setText("")
        self.registro.txtCuota.setText("")
        self.registro.checkInternacional.setChecked(False)


### reportar fichaje ###
    def llenarComboPaises(self):
        objData = paisData()
        datos = objData.listaPaises()
        for pais in datos:
            self.reporte.boxPais.addItem(pais[1])          
