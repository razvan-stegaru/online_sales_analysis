from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 3500.00, 5))
manager.add_product(Product("Telefon", 2500.00, 10))
manager.add_product(Product("Casti Wireless", 400.00, 15))

manager.display_products()
print(f"\nValoarea totală a inventarului: {manager.total_inventory_value():.2f} RON")
