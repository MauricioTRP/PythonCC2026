def greeting(name):
    """
    This function greets a person
    using it's name as parameter
    """
    # print(f"Hello {name} good morning!")
    return "Hello " + name + " Good morning!"

def absolute_value(num):
    """
    This function return the absolut value
    of a number
    
    :param num: The number to be returned in absolute value
    """
    if num >= 0:
        return num
    else:
        return -num

absolute_of_x = absolute_value(-45)

muestras = [12, -15, 0, 0, -4.9, 1]

abs_muestras = [ absolute_value(muestra) for muestra in muestras ]

print(muestras)
print(abs_muestras)
print(sum(abs_muestras))

# print(absolute_of_x)



# def function_name(parameters):
#     """Doc String"""
#     # statements
#     return [expresiones]

# greetingMessage = greeting("Constanza")

# la documentación se almacena en la propiedad
# __doc__

# print(greeting.__doc__)
# print(greetingMessage)