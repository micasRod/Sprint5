lista = [3, "Hola", "Mundo", 5]

def agregar_una_vez(lista, el):
    try:
        
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
            print(lista)
    except ValueError:
        print(f"Error: Imposible añadir elementos duplicados => {el}")
        

agregar_una_vez(lista, 5)
agregar_una_vez(lista, 10)
agregar_una_vez(lista, -2)
agregar_una_vez(lista, "Hola")


    


        
        

