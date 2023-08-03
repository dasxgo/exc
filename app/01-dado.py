import random

def obtener_numero_aleatorio():
    return random.randint(1,6)

if __name__ == '__main__':
    numero = obtener_numero_aleatorio()
    print('El numero aleatorio es:', numero)