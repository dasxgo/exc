# utils.py

def mult(a, b):
    multiplicacion = a * b
    return multiplicacion

def suma(a, b):
    suma = a + b
    return suma

def resta(a, b):
    resta = b - a
    return resta

if __name__ == '__main__':
    print(f'el resultado de la operacion es =>', mult(2, 5))
    print('=' * 64)
    print(suma(8, 9))
    print(f'el resultado de la resta =>', resta(20, 10))


