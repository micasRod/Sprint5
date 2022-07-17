
import json
from typing_extensions import Self
from clases import *
import codecs


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

class LeerJson:
    archivoJson= input("Ingrese el nombre del archivo json")

    def init(self) -> None:
        pass

    def abrirArchivo(archivoJson):
        with open(archivoJson) as file:
            datos=json.loads(file.read())
        return datos

class Crear_HTML:
    import codecs

archivoHTML= input("ingrese nombre del archivo que desea crear")

archivoHTML=archivoHTML+".html"
f=open(archivoHTML,'w')

html_template="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Hola</p>
</body>
</html>
"""
f.write(html_template)

f.close()

file = codecs.open(archivoHTML, 'r', "utf-8")

print(file.read())