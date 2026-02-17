SPEED_OF_LIGHT = 299_792_458 # GLOBAL
PI = 22/7
GRAVITY = 9,27

# Las funciones pueden tener mas de un argumento
def greet(name, msg = "bienvenid@ al curso de Python"):
    """
    Esta funcion saluda usando el nombre y un mensaje de saludo
    
    :param name: Nombre de la persona
    :param msg: Mensaje que se usará para saludar
    """
    print(f"Hola {name}, {msg}")

# greet("Monica", "Chandler te está esperando")
# greet("Curso", "estamos aprendiendo python")

# greet(msg= "Sin mensaje",name = "Erika")

# greet("Carlos", msg= "Esto funciona")
# greet(name="Carlos", "esto no funciona")

def green_many_people(*names):
    """
    This function salutes many people
    
    :param names: one or many names
    """
    for name in names:
        print(f"Hello {name}")

# green_many_people("Carlos", "Erika", "Sebastián", "Fernanda")

# operador "*" indica que desde ese parámetro en adelante
# "coleccionará" todos los argumentos extra en una colección de tipo
# tupla
def print_one_or_many_numbers(first_arg, second_arg,*rest_of_args):
    print(f"argument 'first': {first_arg}")
    print(f"argument 'second': {second_arg}")
    
    print(type(rest_of_args))
    print(f"argument: 'rest_of_args' {rest_of_args}")
    for arg in rest_of_args:
        print(f"arg: {arg}")

print_one_or_many_numbers(10, 123,1, 23, 12, 123)
