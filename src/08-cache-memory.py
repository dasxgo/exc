import time
from joblib import Memory

cache = Memory(location='C:/cache')

@cache.cache
def funcion_compleja(primer_1, segundo_2):
    time.sleep(4)
    print(f'calculando')
    return primer_1 + segundo_2

resultado = funcion_compleja(2,2)
print(f'El resultado es: {resultado}')