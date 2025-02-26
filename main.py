from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop Gaming", 3500.00, 3))
manager.add_product(Product("Smartphone", 2500.00, 5))
manager.add_product(Product("Casti Bluetooth", 400.00, 10))

manager.display_products()
print(f"\nValoarea totală a inventarului: {manager.total_inventory_value():.2f} RON")
