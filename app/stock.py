class Inventory:
    def __init__(self):
        self.items = {}

    def add_items(self, id_item, name_product, stock_quantity, price):
        self.items[id_item] = {'name_product': name_product,
                                       'quantity': stock_quantity,
                                       'price': price}

    def update_items(self, id_item, name_product, stock_quantity, price):
        if id_item in self.items:
            self.items[id_item] = {'name_product': name_product,
                                           'stock_quantity': stock_quantity,
                                           'price': price}
        else:
            print("The item is not in inventory..")

    def check_item_details(self, id_item):
        return self.items.get(id_item, "Item not found in inventory")

# Create an object of class Inventory
my_inventory = Inventory()
print(f'inventario inicial:', my_inventory.items)
print('='*120)

# Add items to inventory
my_inventory.add_items('001', 'Apple', 100, 0.5)
my_inventory.add_items('002', 'Orange', 80, 0.3)

print(f'Add Items:', my_inventory.items)
print('='*120)

# Check item details
print(f'Check Item:', my_inventory.check_item_details('001'))
print('='*120)


# Update item details
my_inventory.add_items('001', 'Apple', 120, 0.5)
print(f'Update Inventory:', my_inventory.items)
