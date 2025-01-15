import conexion as con 
from model.movimiento import Transferencia
from datetime import datetime

class TransferenciaData():

    def __init__(self)-> None:
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_transferencias = '''CREATE TABLE IF NOT EXISTS transferencias(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    monto NUMERIC,
                    clubOrigen TEXT,
                    cuota NUMERIC,
                    internacional BOOLEAN,
                    verificado BOOLEAN,
                    fecha DATETIME)'''
            self.cursor.execute(sql_create_transferencias)
            self.db.commit()
            self.cursor.close()
            self.db.close
            print("Tabla transferencias OK")

        except Exception as e:
            print("Tabla transferencias OK:", e)

    def registrar(self, info:Transferencia):
        fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        resultado = self.cursor.execute("""
        INSERT INTO transferencias(monto, clubOrigen, cuota, internacional, verificado, fecha) VALUES(?,?,?,?,?,?)""", (info.monto, info.clubOrigen, info.cuota, info.internacional, False, fecha))
        self.db.commit()
        if self.cursor.rowcount == 1:
            return True
        else:
            return False
      