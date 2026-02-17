# Recursion: funciones que se llaman a si mismas

def rec(in_param):
    if (in_param < 5):
        print(in_param)
        rec(in_param + 1)

# rec(1)

def calc_factorial(x):
    """Recursive function to find factorial of x"""
    if x == 0:
        return 1
    else:
        return (x * calc_factorial(x - 1))
    
num = 5
print(f"El factorial de {num} = {calc_factorial(num)}")

# calc_factorial(5)                         primera llamada
# 5 * calc_factorial(4)                     segunda llamada
# 5 * 4 * calc_factorial(3)                 tercera llamada
# 5 * 4 * * 3 * calc_factorial(2)           cuarta llamada
# 5 * 4 * * 3 * 2 * calc_factorial(1)       quinta llamada
# 5 * 4 * * 3 * 2 * 1 * calc_factorial(0)   sexta llamada
# 5 * 4 * * 3 * 2 * 1 * 1                   retorno sexta
# 5 * 4 * * 3 * 2 * 1                       retorno quinta
# 5 * 4 * * 3 * 2                           retorno cuarta
# 5 * 4 * * 6                               retorno tercera
# 5 * 24                                    retorno segunda
# 120                                       retorno primera

