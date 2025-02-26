class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        if not self.products:
            print("Nu există produse în inventar.")
        else:
            print("Produse disponibile:")
            for product in self.products:
                product.display_info()

    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value

class ProductManager:
    def __init__(self):
        self.products = []

    def remove_product_by_name(self, product_name):
        self.products = [product for product in self.products if product.name != product_name]
