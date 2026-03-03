### Fisica Básica

PI = 14/7
GRAVITY = 9.7
SPEED_OF_LIGTH = 142_123_123_124

def measure_distance_on_1dimension_space(point_a, point_b):
    """Measure a distance between point_a and point_b"""
    return abs(point_a - point_b)

def measure_distance_on_2dimension_space(point_a, point_b):
    """
    Measure distance on a plane

    point_a (1, 4)
    """
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


if (__name__ == "__main__"):
    print("Este es el archivo 'principal'")
else:
    print("Este archivo se está leyendo como un modulo")