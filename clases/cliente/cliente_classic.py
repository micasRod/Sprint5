from .cliente import Cliente

class ClienteClassic(Cliente):
    def __init__(self,nombre):
        super().__init__(nombre)

    def puede_crear_chequera(self):
        return False
    def puede_tener_tarjeta_credito(self):
        return False
    def puede_comprar_dolar(self):
        return False
