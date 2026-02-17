import math # importación

lista_supermercado = ["huevo", "queso", "jamón", "palta"]

def say_hi(name = ""):
    print(f"Hi {name}")

# for elemento_lista in lista_supermercado:
#     print(f"Debes comprar {elemento_lista.capitalize()}")


# saluda hasta escribir "exit"

# name = input("Please enter your name")

def greet_while_not_exit(name):
    print(f"Hi {name} nice to meet you")


# while (name != "exit"):
#     # mientras la condición sea verdad
#     greet_while_not_exit(name=name)
#     name = input("Please enter other name")

# rangos

number_upto_10 = range(11) # -> llega hasta 11 - 1exit

numbers_from_5_to_10 = range(5, 11) ## [5, 10]
pair_numbers_from_2_to_20 = range(2, 21, 2)

def square_root_of(number):
    return math.sqrt(number)

# print(list(number_upto_10))
# print(list(numbers_from_5_to_10))
# print(list(pair_numbers_from_2_to_20))

for pair_number in pair_numbers_from_2_to_20:
    print(f"The square root of {pair_number} is: {square_root_of(pair_number)}")


# tenemos prohibido continuar si aparece el caracter "Z"
contrasena = "as1AOSIDUZOIUOI"

for letra in contrasena:
    if letra == 'Z':
        break
        # continue

    print(f"La letra actual es {letra}")

sequence = {'P', 'a', 's', 'w'}

for letter in sequence:
    pass ## no está implementado => no ejecutar


