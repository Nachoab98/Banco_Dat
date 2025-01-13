import sqlite3

class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect('banco.db')
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
            sql_create_table = '''CREATE TABLE IF NOT EXISTS usuario(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    usuario TEXT unique,
                    clave TEXT)'''
            cur= self.con.cursor()
            cur.execute(sql_create_table)
            cur.close()
            self.crearAdmin()

    def crearAdmin(self):
            try:
                sql_insert ='''INSERT INTO usuario(nombre, usuario, clave) VALUES('administrador', 'admin', 'admin2025')'''
                cur= self.con.cursor()
                cur.execute(sql_insert)
                cur.close()
                self.con.commit()
            except Exception as ex:
                 print(ex)
    
    def conectar(self):
        return self.con
                 

