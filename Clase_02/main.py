GRAVITY_ACCELERATION = 9.8
PI = 3.14
SPEED_OF_LIGHT = 65435546876854356476864 # ESTO NO PUEDE SER CAMBIADO!!!!! 

myBigNumber = 1 + 5 + 8 +       \
        4 + 3 + 5 + 6 + 2 +     \
        27 + 8 + 9 + 7 + 7 +    \
        6 + 4

myOtherNumber = ( 1 + 3 + 64 + 5 +
                 3 + 50 + 10 )


books = {
    "987-10-6-4561-2": "Crónicas del pájaro que da cuerda al mundo",
    "652-4-50-4565-4": "Cazando un carnero"
}

music = {
    0x10ff00: "Chopin - Nocturne 3",
    0x10ff01: "Chopin - Nocturne 2"
}

# print(myBigNumber)
# print(myOtherNumber)

x = 5
temperatura_en_el_espacio = (3, 4, 5, 30)
mi_lista_supermercado = ["Pan", "Palta", "Queso"]

# Podemos escribir la variable "mi lista surpermercado" de 3 formas
# 
# camelCase -> miListaSupermercado
# snakeCase -> mi_lista_supermercado
# kebabCase -> mi-lista-supermercado
#
#  Recomendación: Mantener una forma de escritura en todo el proyecto

def showAddressInMemory(someVariable):
    print(hex(id(someVariable)))


showAddressInMemory(x)
showAddressInMemory(mi_lista_supermercado)
showAddressInMemory(temperatura_en_el_espacio)

x = 6
mi_lista_supermercado.append("café")
showAddressInMemory(x)
showAddressInMemory(mi_lista_supermercado)

# if myBigNumber > 100:
#     print("My big number is bigger than 100")
#     if myOtherNumber > myBigNumber:
#         print("My big number isn't as big as my other number")


# # imprime el tipo de dato de mi variable
# print("La variable temperatura_en_el_espacio es de tipo: ")  
# print(type(temperatura_en_el_espacio))

# print("La variable mi_lista_supermercado es de tipo: ", type(mi_lista_supermercado))

# # Mostramos la dirección de las variables


