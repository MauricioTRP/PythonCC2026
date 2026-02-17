name = "Pepe"
age = 31
last_name = "González"

# print("El nombre del usuario es %s %s tiene edad %i", name, last_name, age)
print("El nombre del usuario es", name, last_name, "tiene edad", age)


# String interpolation
print(f"El nombre del usuario es {name} {last_name} tiene edad {age}")
print(f"el próximo año tendrá {age + 1.7}")


dia_seleccionado = 'martes'

match dia_seleccionado:
    case 'sabado':
        print("Te puedes ir de fiesta, mañana no trabajas")
    case 'domingo':
        print("Te recomiendo no fiestear hoy, mañana trabajas")
    case _:
        print("Día laboral")


def check_http_status(status):
    if status in range(200, 300):
        print("Success")
    elif status in range(400, 500):
        print("Client error")
    else:
        print("Server Error")

# check_http_status(240)
# check_http_status(404)
# check_http_status(500)

def check_error_status_v2(status):
    match status:
        case 404:
            print("Not found")
        case 403:
            print("Unauthorized")
        case 400:
            print("Bad request")
        case _:
            print("Unknown error")

# check_error_status_v2(408)
# check_error_status_v2(404)

http_status_response = input("Which is the response code")

check_error_status_v2(http_status_response)
