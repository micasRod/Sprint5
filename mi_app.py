from clases import *


# cliente = ClienteBlack()
# print(cliente.puede_tener_chequera())

def creador_cliente():
    return [ClienteBlack("Nicolas"), ClienteClassic("Matias"), ClienteClassic("Agus")]

misClientes = creador_cliente()

for cliente in misClientes:
    if cliente.puede_tener_chequera():
        print("El cliente {} puede tener chequera".format(cliente.get_nombre()))
    else:
        print("El cliente {} no puede tener chequera".format(cliente.get_nombre())) 

