# importar módulo completo
# import <module_name> [, <module_name_1>, <module_name_2>, ...]
import fisics, os

point_1 = 15
point_2 = -20

# distance = fisics.measure_distance(point_1, point_2)

# print(distance)

# print(os.getcwd())


# IMPORTAR SÓLO ALGUNOS ELEMENTOS DEL MÓDULO
# from <module_name> import <name1> as <alt_name1>   [, <name2> as <alt_name2>, <name3> as <alt_name3>, ...]
from fisics import measure_distance_on_2dimension_space as distance_2d, GRAVITY

point_a = (1, 4)
point_b = (0,2)

distancia_2 = distance_2d(point_a, point_b)

# print(distancia_2)
# print(GRAVITY)

print(f"fisics.__name__ from 'main.py:27': {fisics.__name__}")
print(f"__name__ from 'main.py:28': {__name__}")

# print(dir())