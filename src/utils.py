def main():

    def mult(a,b):
        multiplicacion = a * b
        return multiplicacion
    print(f'el resultado de la operacion es =>', mult(2,5))

    print('='*64)

    def sum(a,b):
        suma = a + b
        return suma

    print(sum(8,9))

def resta(a,b):
    resta = b - a
    return resta

print(f'el resultado de la resta =>', resta(20,10)) 


if __name__ == '__main__':
    main()