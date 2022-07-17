from .cliente import Cliente

class ClienteBlack(Cliente):
    def puede_crear_chequera(self):
        return True
    def puede_tener_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True
