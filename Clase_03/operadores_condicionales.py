# if: "si pasa esto, -> "
# elif: else if "si pasa esta otra cosa ->"
# else: "en otro caso ->"

user1Age = 18
user2Age = 15

print("user1Age > user2Age", user1Age > user2Age)

def checkAdulthood(user):
    if (user >= 18):
        print("User is an adult")
    else:
        print("Is not an adult")

checkAdulthood(user1Age)
checkAdulthood(user2Age)


# Modelando si uso abrigo grueso o liviano para lluvia
temp = 17
lluvia = True

def checkIfShouldUseJacket(temp, isRaining = True):
    if (temp < -1 and isRaining): # revisar convenciones respecto a condicionales
        print("Must wear thick jacket")
    elif temp >= -1 and isRaining:
        print("Must wear light jacket")
    else:
        print("Can go without jacket")
    
checkIfShouldUseJacket(temp=temp, isRaining=lluvia)

# Identity operators
# is -> "es esta variable"
# is not -> "no es 'esta variable'"

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

def printAddress(variable):
    print(hex(id(variable)))

printAddress(x1)
printAddress(y1)
print(x1 is y1)
print("--------------------")
printAddress(x2)
printAddress(y2)
print(x2 is y2)
print("\n--------------------")
printAddress(x3)
printAddress(y3)
print("x3 is y3", x3 is y3)
print("x3 is not y3", x3 is not y3)
print("x3 == y3", x3 == y3)

listaSupermercado = ['Café', 'Pan', 'Tomate']

if ('Palta' in listaSupermercado):
    print("Vamos bien")
else:
    print("No puedo desayunar así")

nombre = 'Chayanne'

if 'n' in nombre:
    print('Chayanne tiene la letra n')




# Repaso 

# dias_semana = set(['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo'])





