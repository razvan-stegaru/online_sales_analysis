class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def total_cart_value(self):
        total_value = sum(product.price * product.quantity for product in self.cart_items)
        return total_value

    def display_cart(self):
        if not self.cart_items:
            print("Coșul este gol.")
        else:
            print("Produse în coș:")
            for product in self.cart_items:
                product.display_info()
