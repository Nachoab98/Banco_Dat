from PyQt6 import uic  #permite convertir el designer a python
from PyQt6.QtWidgets import QMessageBox
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
        self.registro = uic.loadUi('designer/registrarFichaje.ui')

    def abrirRegistrarFichaje(self):
        self.registro.btnRegistrar.clicked.connect(self.registrarTransaccion) #se ejecuta solo cuando se interactua con el boton
        self.registro.show()
    
    def registrarTransaccion(self):   
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
        else:
            mBox.setText("Error al realizar la transferencia")
        mBox.exec()

        
