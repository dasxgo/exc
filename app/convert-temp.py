def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5)

def celsius_a_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit -32) * 5/9

def fahrenheit_a_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_a_celsius(kelvin):
    return kelvin - 273.15

def kelvin_a_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def obtener_unidad_temperatura():
    unidades_validas = [ 'c', 'f', 'k']
    while True:
        unidad = input("Ingresa la unidad de temperatura (celsius 'c', fahrenheit 'f', kelvin 'k'): ")
        if unidad in unidades_validas:
            return unidad
        else: 
            print("Unidad de temperatura invalida. Por favor elige entre 'c', 'f' o 'k'. ")
def  obtener_grado():
    while True:
        try: 
            grado = float(input("Ingresa el valor de la temperatura: "))
            return grado 
        except ValueError:
            print("Valor invalido. Ingresa un numero valido")
def main():
    print("Bienvenido al conversor de temperatura")
    unidad_original = obtener_unidad_temperatura()
    unidad_destino = obtener_unidad_temperatura()
    grado = obtener_grado()

    if unidad_original == 'c':
        if unidad_destino == 'f':
            resultado = celsius_a_fahrenheit(grado)
        elif unidad_original == 'k':
            resultado = celsius_a_kelvin(grado)
    elif unidad_original == 'f':
        if unidad_destino == 'c':
            resultado = fahrenheit_a_celsius(grado)
        elif unidad_destino == 'k':
            resultado = fahrenheit_a_kelvin(grado)
    elif unidad_original == 'k':
        if unidad_destino == 'c':
            resultado = kelvin_a_celsius(grado)
        elif unidad_destino == 'f':
            resultado = kelvin_a_fahrenheit(grado)
    
    print(f'{grado} grados {unidad_original.upper()} es igual a {resultado:2f} grados {unidad_destino.upper()}')

if __name__ == '__main__':
    main()        



