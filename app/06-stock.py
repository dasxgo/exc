class Inventario:
    def __init__(self):
        self.articulos = {}

    def agregar_articulos(self, id_articulo, nombre_articulo, cantidad_stock, precio):
        self.articulos[id_articulo] = {'nombre_articulo': nombre_articulo,
                                       'cantidad_stock': cantidad_stock,
                                       'precio': precio}

    def actualizar_articulo(self, id_articulo, nombre_articulo, cantidad_stock, precio):
        if id_articulo in self.articulos:
            self.articulos[id_articulo] = {'nombre_articulo': nombre_articulo,
                                           'cantidad_stock': cantidad_stock,
                                           'precio': precio}
        else:
            print("El artículo no se encuentra en el inventario.")

    def verificar_detalles_articulo(self, id_articulo):
        return self.articulos.get(id_articulo, "Articulo no encontrado en el inventario")

# Crear un objeto de la clase Inventario
mi_inventario = Inventario()
print(f'inventario inicial:', mi_inventario.articulos)
print('='*120)

# Agregar articulos al inventario
mi_inventario.agregar_articulos('001', 'Manzana', 100, 0.5)
mi_inventario.agregar_articulos('002', 'Naranja', 80, 0.3)

print(f'Agregacion articulos:', mi_inventario.articulos)
print('='*120)

# Verificar los detalles del articulo
print(f'Verificacion articulo:', mi_inventario.verificar_detalles_articulo('001'))
print('='*120)


# Actualizar detalles del articulo
mi_inventario.actualizar_articulo('001', 'Manzana', 120, 0.5)
print(f'Inventario actualizado:', mi_inventario.articulos)
