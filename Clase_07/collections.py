lista_supermercado = ["pan", "arroz", "fideos", "gnocci"]

# [ <computo> for <elemento> in <Collection> ] -> crea nueva lista con base en la collection
lista_capitalized = [ item.capitalize() for item in lista_supermercado ]

print(lista_supermercado)
print(lista_capitalized)

# hacemos descuento si lleva arroz
lista_validando_si_es_arroz = [ item == 'arroz' for item in lista_supermercado ]
print(lista_validando_si_es_arroz)
trae_arroz_la_lista = any(lista_validando_si_es_arroz)

print(f"El usuario trae arroz {trae_arroz_la_lista}")
# all_true = [True, True, True]
# any_true = [ False, True, False, False ]

# print(f"all(all_true) {all(all_true)}")
# print(f"all(any_true) {all(any_true)}")
# print(f"any(all_true) {any(all_true)}")
# print(f"any(any_true) {any(any_true)}")
