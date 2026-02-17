def address_of(x):
    print("The address of the variable is: ",hex(id(x)),"\n and the value is: ", x)

todos_true = [True, True, True, True, False]

print(all(todos_true))

todos_true[2:4]
todos_true[:3]
todos_true[4:]


# copia de listas (independiente distinto de clonar)

l1 = [1, 2, 3]
l2 = l1 # clon del simbolo

l3 = l1[:] # "trasvacijar" elementos de un list a otro

# address_of(l1)
# address_of(l2)
# address_of(l3)

l1[2] = "Tree 🌳"
print("\n............................\n")
# address_of(l1)
# address_of(l2)
# address_of(l3)




list_felipe = ["arroz", "fideos", "pasta de tomates", "fideos", "fideos"]
list_fernanda = ["pan", "queso", "galletas", "arroz", "fideos"]
list_mauricio = ["cepillo", "arroz", "jamon", "palta", "fideos", "fideos"]
list_erika = ["pan", "mermelada", "tostador"]
list_mauricio.append("queso")

lista_a_procesar = [list_felipe, list_fernanda, list_mauricio, list_erika]

have_rice = [ item == "arroz" for item in list_mauricio ]
print(f"La lista de mauricio tiene arroz {any(have_rice)}")


# # revisar si hay cosas repetidas "fideos"
# for list_cliente in lista_a_procesar:
#     cantidad_fideos = list_cliente.count("fideos")

#     if cantidad_fideos >= 2:
#         print("Lleva muchos fideos")
#     else:
#         print("Cantidad adecuada")


# sacamos arroz de las listas
# for client_list in lista_a_procesar:
#     try:
#         # 1 buscamos la posición del "arroz" dentro de esta lista
#         index_arroz = client_list.index("arroz")

#         # 2 eliminamos el elemento en la posición "index_arroz"
#         mensaje_arroz = client_list.pop(index_arroz) # elimina el arroz, y lo pasa a la variable

#         # 3 imprimimos un mensaje
#         print(f"No hay {mensaje_arroz} en inventario, por lo tanto lo eliminamos de la posición {index_arroz}")
#     except:
#         print("No había arroz en la lista, continuamos")


# for client_list in lista_a_procesar:
#     client_list.sort()
#     client_list.reverse()
#     print("productos del cliente: ", client_list)
#     print("El arroz se encuentra en la posicion", client_list.index("arroz"))


# # mutables
# # los cambios que se hacen
# # son el "el mismo objeto en memoria"


# my_list = [True, "MyString", 123, 153.5, [1, 2, 3, False]]

# # my_list[4] = "Nuevo elemento"
# # append agrega al final
# my_list.append("elemento al final")
# # insert
# my_list.insert(1, "nuevo elemento en la posición 1")

# lista_de_elementos_para_agregar = ["me olvidé de esto", " y de esto otro"]

# my_list.extend(lista_de_elementos_para_agregar)

# print(my_list)
# print("Tamaño de la lista my_list: ", len(my_list))
# # print(my_list[1])
# # print(my_list[-4])  
# # comentar una linea CTRL + }

# my_string = "my string"

# # print(my_string[3])
# # print(my_string[-5])

# # address_of(my_list)

# # x = all(my_list) # retorna booleano en caso que sea iterable

# # print(x)

# # my_list.append(['nested', 'list'])

# # print("antes de crear la copia")
# # address_of(my_list)

# # copia_lista = my_list

# # copia_lista.append(5)

# # print("\nMi copia:")
# # address_of(copia_lista)
# # print("\nMi lista original:")
# # address_of(my_list)