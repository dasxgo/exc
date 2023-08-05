class Carrito:
    def __init__(self):
        self.articulos = []
    
    def agregar_articulos(self, articulo, precio):
        self.articulos.append({'articulo': articulo, 
                           'precio': precio})
    def remover_articulo(self, articulo):
        for item in self.articulos:
            if item['articulo'] == articulo:
                self.articulos.remove(item)
                break
    def calcular_total(self):
        total = 0 
        for item in self.articulos:
            total += item['precio']
            return total


# Primero creamos una instancia de carrito 

mi_carrito = Carrito()
print(mi_carrito.articulos)

print('='*120)

# Vamos agregar algunos articulos
mi_carrito.agregar_articulos('Manzanas', 5.00)
mi_carrito.agregar_articulos('Naranjas', 3.00)
mi_carrito.agregar_articulos('Manzanas', 4.00)
print(mi_carrito.articulos)

print('='*120)

# Ahora si queremos remover un articulo
mi_carrito.remover_articulo('Naranjas')
print(mi_carrito.articulos)

print('='*120)

# Calcular el total
total = mi_carrito.calcular_total()
print(f'El total del carrito es =>:', total)


