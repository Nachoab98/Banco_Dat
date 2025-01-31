import conexion as con 
from model.movimiento import Reporte
from datetime import datetime

class ReporteData():

    def __init__(self)-> None:
        try:
            self.db = con.Conexion().conectar()
            self.cursor = self.db.cursor()
            sql_create_reportes = '''CREATE TABLE IF NOT EXISTS reportes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT,
                    doc TEXT,
                    nombre TEXT,
                    apellido TEXT,
                    genero TEXT,
                    deporte TEXT,
                    pais TEXT,
                    fecha DATETIME,
                    terminos BOOLEAN)'''
            self.cursor.execute(sql_create_reportes)
            self.db.commit()
            print("Tabla reportes creada o ya existe")
        except Exception as e:
            print("Error al crear la tabla reportes:", e)
        finally:
            self.cursor.close()
            self.db.close()  # Asegúrate de cerrar la conexión correctamente

    def reportar(self, info: Reporte):
        diaReporte = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.db = con.Conexion().conectar()
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute("""
            INSERT INTO reportes(tipo, doc, nombre, apellido, genero, deporte, pais, fecha, terminos, diaReporte) VALUES(?,?,?,?,?,?,?,?,?,?)""", 
            (info.tipo, info.doc, info.nombre, info.apellido, info.genero, info.deporte, info.pais, info.fecha, info.terminos, diaReporte))
            self.db.commit()
            if self.cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception as e:
            print("Error al reportar:", e)
            return False
        finally:
            self.cursor.close()
            self.db.close()  # Asegúrate de cerrar la conexión correctamente