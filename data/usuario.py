import conexion as con 
from model.usuario import Usuario

class UsuarioData():

    def __init__(self):
        try:
            self.con = con.Conexion().conectar()
            self.cursor = self.con.cursor()
            sql_insert ='''INSERT INTO usuario(nombre, usuario, clave) VALUES('administrador', 'admin', 'admin2025')'''
            self.cursor.execute(sql_insert)
            self.cursor.close()
            self.con.commit()
        except Exception as ex:
            print(ex)

    def login(self, usuario:Usuario):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        resultado = self.cursor.execute("SELECT * FROM usuario WHERE usuario = '{}' AND clave = '{}'".format(usuario.usuario, usuario.clave))
        fila= resultado.fetchone()
        if fila:
            usuario = Usuario(nombre=fila[1], usuario=fila[2])
            self.cursor.close()
            self.db.close()
            return usuario
        else:
            self.cursor.close()
            self.db.close()
            return None