def obtener_numero():
    while True:
        try:
            numero = int(input('ingresa un numero entero:'))
            return numero
        except ValueError:
            print('Valor invalid. Ingrese un numero entero valido')

def mostrar_tabla_multiplicar(numero):
    print('tabla de multiplicar del {numero}:')
    for i in range(1,11):
        resultado = numero * 1
        print(f'(numero) * {i} = {resultado}')

def main():
    print('Bienvenido a la tabla de multiplicar')
    numero = obtener_numero()
    mostrar_tabla_multiplicar(numero)

if __name__ == '__main__':
    main()