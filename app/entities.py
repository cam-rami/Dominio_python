
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

class cupo():
    def __init__(self, letra):
        self.letra = letra

class pago():
    def __init__(self, fecha_inicio, hora_inicio, fecha_fin, hora_fin, valor, carro, cupo, empleado):
        self.fecha_inicio = fecha_inicio
        self.hora_inicio = hora_inicio
        self.fecha_fin = fecha_fin
        self.hora_fin = hora_fin
        self.valor = valor
        self.carro = carro
        self.cupo = cupo   
        self.empleado = empleado     

class empleado():
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo 
