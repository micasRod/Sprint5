from .cliente import Cliente

class ClienteBlack(Cliente):
    def puede_tener_chequera(self):
        return True