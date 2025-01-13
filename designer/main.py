from PyQt6 import uic  #permite convertir el designer a python
from PyQt6.QtWidgets import QMessageBox
from designer import registrarFichaje

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

        elif self.registro.txtClub.text() == "":
            mBox= QMessageBox()
            mBox.setText("Ingrese el club")
            mBox.exec()

        elif self.registro.txtCuota.text() == "":
            mBox= QMessageBox()
            mBox.setText("Ingrese la/s cuota/s")
            mBox.exec()

        
        elif self.registro.txtMonto.text() == "":
            mBox= QMessageBox()
            mBox.setText("Ingrese el monto")
            mBox.exec()
        
