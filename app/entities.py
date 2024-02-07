
class Carro():

    #metodo constructor
    placa = "SDF 456"
    tipo_vehiculo = "camion"
    
    #metodo constructor
    def __init__(self, placa, tipo_vehiculo):
        self.placa = placa 
        self.tipo_vehiculo = tipo_vehiculo 

class Cliente():
    def __init__(self, nombre, celular, identificacion, lista_carros):
        self.nombre = nombre
        self.celular = celular
        self.identificacion = identificacion
        self.lista_carros = lista_carros
    
    def addcar(self , car):
        self.lista_carros.append(car)
    
    def listcar(self):
        for i in self.lista_carros:
            print("carro con placa: " + i.placa )