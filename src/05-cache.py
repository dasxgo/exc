import time
from functools import lru_cache
'''
@lru_cache(maxsize=12)
def funcion_compleja(numero1, numero2):
    time.sleep(5)
    print('Ejecutando operacion', 'compleja')
    return numero1+numero2

resultado = funcion_compleja(2,2)
print(f'El resultado es: {resultado}')
resultado = funcion_compleja(2,2)
print(f'El resultado es: {resultado}')
resultado = funcion_compleja(2,2)
print(f'El resultado es: {resultado}')
resultado = funcion_compleja(2,2)
print(f'El resultado es: {resultado}')
'''

def funtion(a,b):
    result = a + b
    return result

print(f'El resultado es =>',funtion(2,2))


