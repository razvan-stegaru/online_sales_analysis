from product import Product
from product_manager import ProductManager
from cart import Cart
import random

manager = ProductManager()

manager.add_product(Product("Laptop", 3500.00, 5))
manager.add_product(Product("Telefon", 2500.00, 10))
manager.add_product(Product("Casti Wireless", 400.00, 15))
manager.add_product(Product("Tableta", 1200.00, 8))
manager.add_product(Product("Monitor", 800.00, 7))

cart = Cart()

selected_products = random.sample(manager.products, 3)
for product in selected_products:
    cart.add_product(product)

cart.display_cart()
print(f"\nValoarea totală de plată a coșului: {cart.total_cart_value():.2f} RON")
