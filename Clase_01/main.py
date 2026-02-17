# comentario de una linea
MY_CONSTANT = 30

# def -> palabra clave para definir una funcion
# numbreDeLaFuncion -> nombre que le damos a la funcion
# () -> parentesis para parametros (si no hay parametros se dejan vacios)
def funcionSaludadora(nombre_usuario):
    """
    Esta es una función que saluda al usuario

    ```python
    funcionSaludadora()  # Llamada a la funcion
    ```
    """
    print("Hola Usuario! " + nombre_usuario)  # Cuerpo de la funcion

    MY_CONSTANT = 20

## Rutina principal
## pedimos al usuario que ingrese su nombre
## por consola, y luego lo saludamos
nombreUsuario = input("Ingresa tu nombre: ")


funcionSaludadora(nombreUsuario)

nombreUsuario2 = input("Ingresa tu nombre")

funcionSaludadora(nombreUsuario2)