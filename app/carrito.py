class Carrito:
    def __init__(self):
        self.products = []
    
    def enter_products(self, product, price):
        self.products.append({'product': product, 
                           'price': price})
    def remove_products(self, product):
        for item in self.products:
            if item['product'] == product:
                self.products.remove(item)
                break
    def calculate_total(self):
        total = 0 
        for item in self.products:
            total += item['price']
        return total

# First we create a cart instance

my_carrito = Carrito()
print(my_carrito.products)
print('='*120)

# Vamos agregar algunos articulos
my_carrito.enter_products('apple', 5.00)
my_carrito.enter_products('oranges', 3.00)
my_carrito.enter_products('strawberry', 4.00)
print(my_carrito.products)
print('='*120)

# Now if we want to remove an article
my_carrito.remove_products('oranges')
print(my_carrito.products)
print('='*120)

# Calculate the total
total = my_carrito.calculate_total()
print(f'The total carrito is =>:',{total})


