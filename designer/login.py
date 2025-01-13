from PyQt6 import uic  #permite convertir el designer a python
from PyQt6.QtWidgets import QMessageBox
from data.usuario import UsuarioData
from designer.main import MainFichaje
from model.usuario import Usuario

class Login():
    def __init__(self):
        self.login = uic.loadUi('designer/login.ui')
        self.iniciarGUI()
        #self.login.btnAcceder.clicked.connect(self.validar)
        self.login.lblError.setText('')
        self.login.show()
    
    def ingresar(self):
        if self.login.txtUsuario.text() == '':
            self.login.lblError.setText('Ingrese un usuario valido')
            self.login.txtUsuario.setFocus()
        elif self.login.txtClave.text() == '':
            self.login.lblError.setText('Ingrese una contraseña valida')
            self.login.txtClave.setFocus()

        else:
            self.login.lblError.setText('')
            usu = Usuario(usuario=self.login.txtUsuario.text(), clave=self.login.txtClave.text())
            usuData= UsuarioData()
            resultado = usuData.login(usu)
            if resultado:
                self.main = MainFichaje()
                self.login.hide()
            else:
                self.login.lblError.setText('Usuario o contraseña incorrectos')
                self.login.txtUsuario.setFocus()
    
    def iniciarGUI(self):
        self.login.btnAcceder.clicked.connect(self.ingresar)