lista_1 = [1, 2, 3]
lista_2 = [3, 4 ,5]
lista_3 = [6, 7 ,8]
lista_completa = [lista_1, lista_2, lista_3]
for client_list in lista_completa:
    try:
        # Intenta hacer esto
        print("la posicion del 2: ", client_list.index(2)) # en qué indice está el número 2
    except:
        # En caso de falla haz esto
        print("No está el 2 en la lista")