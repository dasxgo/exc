
# Recorriendo frutas en bucle for

frutas = ['manzana', 'banana', 'certeza', 'durazno']

for fruta in frutas:
    print(fruta)

print('='* 64)

# Recorriendo una lista y obteniendo indice con enumarate

for index, fruta in enumerate(frutas):
    print(f'fruta {index + 1}: {fruta}')

print('='* 64)

## Recorrido al reves de una lista

for fruta in reversed(frutas):
    print(fruta)

 
print('='* 64)   

# Recorrer una lista ordenada

for fruta in sorted(frutas):
    print(fruta)



