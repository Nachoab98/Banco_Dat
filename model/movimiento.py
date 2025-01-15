class Transferencia():
    def __init__(self, tipo:str, clubOrigen:str, monto:float, cuota:int, internacional: bool):
        self.tipo = tipo
        self.clubOrigen = clubOrigen
        self.monto = monto
        self.cuota = cuota
        self.internacional = internacional