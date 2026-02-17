my_set = { 1, 3, 6, 6, 6, 6 }

print(my_set)

lista_asistencia = [ 'Bruno', 'Romina', 'Bruno' ]

print(f"lista en bruto de asistencia {lista_asistencia}")

lista_filtrada_conexiones_unicas = set(lista_asistencia)

print(f"lista filtrada {lista_filtrada_conexiones_unicas}")

amigos_romina = { 'Isidora', 'Bruno', 'Alvaro', 'Valentina' }
amigos_johan = { 'Bruno', 'David', 'Constanza', 'Sebastian' }

# intersección: &

amigos_en_comun = amigos_johan & amigos_romina

print(f"tipo de dato en variable 'amigos_en_comun' {type(amigos_en_comun)}")

# operador direfencia: -
amigos_no_compartidos = amigos_johan - amigos_romina # amigos que tiene Johan, y que no tiene Romina
print(amigos_no_compartidos)

# union: |
todos_los_amigos_para_la_fiesta = amigos_johan | amigos_romina
print(todos_los_amigos_para_la_fiesta)

eliminado = todos_los_amigos_para_la_fiesta.pop()

print(todos_los_amigos_para_la_fiesta)
print(f"amigo eliminado {eliminado}")
