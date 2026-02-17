# def my_function:
#       bloque interno

x = "Azul "

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

contador1 = make_counter()
contador2 = make_counter()

print(contador1())
print(contador1())
print(contador1())
print(contador1())

print(contador2())
print(contador2())


# def una_funcion():
#     # interno a la función
#     global x
#     x = x + x
#     print(f"Llamando x internamente: {x}")

# una_funcion()
# print(f"Llamando x de forma Global: {x}")
