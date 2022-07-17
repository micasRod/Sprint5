from numpy import diag_indices
class Cliente:
    def __init__(self,nombre,apellido,dni,numeroCliente,direccion):
        self.nombre = nombre
        self.apellido= apellido
        self.dni=dni
        self.numeroCLiente= numeroCliente
        self.direccion=Direccion()
    def puede_crear_chequera(self):
        return False
    def puede_tener_tarjeta_credito(self):
        return False
    def puede_comprar_dolar(self):
        return False



class Direccion():
    def __init__(self,calle,numero,ciudad,provincia,pais) :
        self.calle=calle
        self.numero=numero
        self.ciudad=ciudad
        self.provincia=provincia
        self.pais=pais
