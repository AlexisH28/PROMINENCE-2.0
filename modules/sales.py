import datetime
import modules.crud as Crud
import modules.users as Users
import modules.products as Products
import modules.services as Services
import modules.tool_tabulate as Tables
import constants.contants as CONSTANTS

def read(base_path, path_db):
    sales = Crud.read_db(base_path, path_db)
    return sales

def create(base_path, sales, available_ps, op_sale, id_ps, type_sale):
    # Determina el id consecutivo de la venta a crear
    max_id = 0
    for sale in sales:
        id_current = sale.get("id", 0)
        max_id = max(max_id, id_current)
        
    max_id += 1
    new_sale = {
        "id": max_id,
        "type_ps": type_sale,
        "id_ps": 0,
        "id_user": 0,
        "cuantity": 0,
        "price_sale": 0,
        "date_sale": "",
        "status": True
    }
    
    ps = [ps_av for ps_av in available_ps if ps_av['id'] == int(id_ps)]
    
    if ps == []: raise Exception("Producto no encontrado")
    
    new_sale['id_ps'] = ps[0]['id']
    
    print()
    print("**** Creación de Venta de "+ str(ps[0]['name']) +" ****")
    print()
    if op_sale == 2: new_sale['cuantity'] = int(input("Digite la cantidad del producto:\n --> "))
    
    # Validar stock exsitente -> cantidad de compra
    if op_sale == 2 and new_sale['cuantity'] > ps[0]['stock']: raise Exception("Cantidad no disponible")
    
    # Validar op_sale para asignar price_sale teniendo en cuenta si es plan/servicio o producto
    if op_sale == 1:
        if type_sale == "plan":
            plans = Services.read(base_path, "/DB/services_plans.json")
            plan = [srv for srv in plans if srv['id'] == id_ps]
            new_sale['price_sale'] = plan['fixed_charge'] * plan['cuantity_days']
        if type_sale == "fiber":
            fibers = Services.read(base_path, "/DB/services_fiber.json")
            fiber = [srv for srv in fibers if srv['id'] == id_ps]
            new_sale['price_sale'] = fiber['price']
    if op_sale == 2:
        products = Products.read(base_path, "/DB/products.json")
        prd = [product for product in products if product['id'] == id_ps]
        new_sale['price_sale'] = prd['price']
     
    print()
    print("** Clientes **")

    users = Users.read(base_path, "/DB/users.json")
    clients = [usr for usr in users if usr['rol'] == "client"]
    # Mostrar usuarios existentes
    Tables.create_table(1, clients, CONSTANTS.HEADERS_USERS)
    op_client = input("1. Cliente Nuevo | 2. Cliente Existente")
    
    if op_client == "1":
        new_user_id = Users.create(base_path, users)
        new_sale['id_user'] = new_user_id
    
    if op_client == "2":
        new_sale['id_user'] = int(input("Digite el ID del cliente existente:\n"))
    
    new_sale['date_sale'] = (datetime.datetime.now()).strftime("%#d-%m-%Y")
    new_sale['status'] = True
    # Creacion de venta
    Crud.create(base_path, "/DB/sales.json", sales, new_sale, "La venta ha sido creada exitosamente")
    # Actualizar Stock del producto
    if op_sale == 2: Products.update_stock(base_path, ps[0]['id'], new_sale['cuantity'])

