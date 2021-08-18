def execute_decorator(func):
    def wrapper(*args, **kwars):
        print('Ingresa tu nombre ')
        func(*args, **kwars)
        print('Gracias por visitarnos')
    return wrapper

@execute_decorator
def ingreso_nombre():
    nombre = input(' ')
    print (f'Hola {nombre} bienvenido')

ingreso_nombre()