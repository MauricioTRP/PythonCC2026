# Booleano: verdadero | falso
# immutable
isUserAdult = False

# Int: números enteros
# immutable
amountOfDishes = 10

# Float: números de coma flotante
# immutable
temperature = 19.5

# list: Secuencia de "objetos" es ordanada
marketList = ["Café", "Palta", "Queso", "Pan", "jamón"]

# tuple: Secuencia inmutable de objetos
temperaturaEnUnLugar = (-70.35, 50.036, 19.5) # (lat, log, temp)
muestraEstatura = ("F", 1.60, 25) # (Genero, Estatura, Edad)

# String: Texto (char char char char char)
myString = "Hello everyone" 

# Set: arreglo de objetos únicos no ordenados
setOfNouns = set(['She', 'He', 'It', 'Elle', 'Nuevo Pronombre'])

setOfNouns.add('Otro pronombre')

# Conjunto "congelado"
COUNTRIES = frozenset(['Argentina', 'Chile', 'Colombia', 'Palestina', 'China'])

# Diccionario: Asocia primer elemento "llave" con un segundo elemento "valor"
books = {
    '123.65.456.54.1': "Crónicas del pájaro que da cuera al mundo",
    '21.456.5.5.4': "La cazería del carnero salvaje"
}
