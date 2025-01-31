class Transferencia():
    def __init__(self, tipo:str, clubOrigen:str, monto:float, cuota:int, internacional: bool):
        self.tipo = tipo
        self.clubOrigen = clubOrigen
        self.monto = monto
        self.cuota = cuota
        self.internacional = internacional

class Reporte():
    def __init__(self, tipo:str, doc:int, nombre:str, apellido:str, genero:str, deporte:str, pais: str, fecha:str, terminos: bool):
        self.tipo = tipo
        self.doc = doc
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        self.deporte = deporte
        self.pais = pais
        self.fecha = fecha
        self.terminos = terminos