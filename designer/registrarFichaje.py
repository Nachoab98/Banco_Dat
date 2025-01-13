from PyQt6 import uic  #permite convertir el designer a python
from PyQt6.QtWidgets import QMessageBox


class registrarFichaje():
    def __init__(self):
        self.registro = uic.loadUi('designer/registrarFichaje.ui')
        self.registro.show()

    