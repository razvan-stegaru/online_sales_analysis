Acest proiect este un sistem de gestionare a produselor și coșurilor de cumpărături, care permite adăugarea, actualizarea și eliminarea produselor. Proiectul folosește Python pentru a implementa logica aplicației.

## Clase
### Product
- **Atribute**: 
  - `name`: numele produsului
  - `price`: prețul produsului
  - `quantity`: cantitatea disponibilă
- **Metode**:
  - `display_info()`: afișează informațiile despre produs
  - `update_quantity()`: actualizează cantitatea de produse

### ProductManager
- **Atribute**:
  - `products`: o listă cu toate produsele disponibile
- **Metode**:
  - `add_product()`: adaugă un produs în lista de produse
  - `display_all_products()`: afișează toate produsele
  - `total_value()`: calculează valoarea totală a tuturor produselor
  - `remove_product()`: elimină un produs după nume

### Cart
- **Atribute**:
  - `cart_items`: lista de produse din coș
- **Metode**:
  - `add_to_cart()`: adaugă produse în coș
  - `calculate_total()`: calculează valoarea totală a coșului
  - `display_cart()`: afișează conținutul coșului