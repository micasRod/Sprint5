lista_Vehiculos = []

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = str(color)
        self.ruedas = int(ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return """ |Coche|
        - Color: {}
        - Ruedas: {}
        - Velocidad: {} km/h
        - Cilindrada: {} cc """.format(self.color, self.ruedas, self.velocidad, self.cilindrada)

mi_Coche = Coche("Rojo", 4, 250, 2800)
mi_Coche2 = Coche ("Gris", 4, 170, 1600)
lista_Vehiculos.append(mi_Coche)
lista_Vehiculos.append(mi_Coche2)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return """ |Bicicleta|
        - Color: {}
        - Ruedas: {}
        - Tipo: {} """.format(self.color, self.ruedas, self.tipo)

mi_Bicicleta = Bicicleta("Negro", 2, "Urbana")
mi_Bicicleta2 = Bicicleta("Rojo", 2, "Urbana")
lista_Vehiculos.append(mi_Bicicleta)
lista_Vehiculos.append(mi_Bicicleta2)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga
    
    def __str__(self):
        return """ |Camioneta|
        - Color: {}
        - Ruedas: {}
        - Velocidad: {} km/h
        - Cilindrada: {} cc 
        - Carga: {} kg """.format(self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga)

mi_Camioneta = Camioneta("Blanco", 4, 150, 2500, 2800)
mi_Camioneta2 = Camioneta("Negro", 4, 180, 5654, 3130 ) 
lista_Vehiculos.append(mi_Camioneta)
lista_Vehiculos.append(mi_Camioneta2)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return """ |Motocicleta|
        - Color: {}
        - Ruedas: {}
        - Tipo: {} 
        - Velocidad: {} km/h
        - Cilindrada: {} cc""".format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindrada)

mi_Motocicleta = Motocicleta("Negro", 2, "Deportiva", 300, 1262)
mi_Motocicleta2 = Motocicleta("Rojo", 2, "Deportiva", 350, 1200)
lista_Vehiculos.append(mi_Motocicleta)
lista_Vehiculos.append(mi_Motocicleta2)

def catalogar(lista_vehiculos, num_ruedas = None):
    contador = 0
    for vehiculo in lista_vehiculos:
        if num_ruedas == int(vehiculo.ruedas):
            print(vehiculo)
            contador += 1
    if num_ruedas:
       print(f"Se han encontrado {contador} vehiculos con {num_ruedas} ruedas.")

catalogar(lista_Vehiculos, 0)
catalogar(lista_Vehiculos, 2)
catalogar(lista_Vehiculos, 4)
