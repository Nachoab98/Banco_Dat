import conexion as con 
from model.usuario import Usuario

class paisData():

    def listaPaises(self):
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        resultado = self.cursor.execute("SELECT * FROM pais order by nombre")
        paises = resultado.fetchall()
        return paises