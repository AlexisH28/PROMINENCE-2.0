import modules.crud as Crud
import modules.tool_tabulate as Tables
import constants.contants as CONSTANTS

def read (base_path, path_db):
    products = Crud.read_db(base_path, path_db)
    return products

def create(base_path, products):
    # Determina el id consecutivo del producto a crear
    max_id = 0
    for product in products:
        id_current = product.get("id", 0)
        max_id = max(max_id, id_current)
        
    max_id += 1
    new_product = {
        "id": max_id,
        "name": "",
        "mark": "",
        "type_product": "",
        "price": 0,
        "warranty": "",
        "stock": 3,
    }
    print()
    print("**** Creación de Producto N: "+ str(max_id) +" ****")
    print()
    new_product['name'] = input("Digite el nombre:\n --> ")
    print()
    new_product['mark'] = input("Digite la marca del producto: \n --> ")
    print()
    new_product['type_product'] = input("Digite el tipo de producto: \n --> ")
    print()
    new_product['price'] = int(input("Digite el precio: \n --> "))
    print()
    new_product['warranty'] = input("Digite la garantía: \n --> ")
    print()
    new_product['stock'] = int(input("Digite las existencias del producto:\n --> "))
    print()
    Crud.create(base_path, "/DB/products.json", products, new_product, "El producto ha sido creado exitosamente")

def update (base_path, products, id):
    for product in products:
        if product['id'] == int(id):
            Tables.create_table(2, product, CONSTANTS.HEADERS_PRODUCTS)
            op_field = 99
            
            while op_field != 0:
                print()
                op_field = input(
                    "Seleccione el campo del producto que desea actualizar:\n" +
                    "1. Nombre | 2. Marca | 3. Tipo de Producto | 4. Precio | 5. Garantía | 6. Existencias | 0. Salir del producto\n --> "
                    )
                print()
                if op_field == "1":
                    name = input("Digite el nombre:\n --> ")
                    print()
                    product['name'] = name
                if op_field == "2":
                    mark = input("Digite la marca del producto:\n --> ")
                    print()
                    product['mark'] = mark
                if op_field == "3":
                    type_product = input("Digite el tipo de producto:\n --> ")
                    print()
                    product['type_product'] == type_product
                if op_field == "4":
                    price = input("Digite el precio:\n --> ")
                    print()
                    product['price'] = int(price)
                if op_field == "5":
                    warranty = input("Digite la garantía:\n --> ")
                    print()
                    product['warranty'] = warranty
                if op_field == "6":
                    stock = input("Digite las existencias del producto:\n --> ")
                    print()
                    product['stock'] = int(stock)
                if op_field == "0":
                    break
                
                Crud.update(base_path, "/DB/products.json", products, "El producto ha sido actualizado exitosamente")
                
def delete(base_path, products, id):
    Crud.delete(base_path, "/DB/products.json", products, id, "El producto ha sido eliminado exitosamente")
    
def update_stock(base_path, id, cuantity_sale):
    products = read(base_path, "/DB/products.json")
    
    for product in products:
        if product['id'] == int(id):
            product['stock'] -= int(cuantity_sale)
            Crud.update(base_path, "/DB/products.json", products, "El producto ha sido actualizado exitosamente")
            break