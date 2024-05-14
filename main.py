import os

import modules.crud as Crud
import modules.users as Users
import modules.tool_tabulate as Tables
import constants.contants as CONSTANTS
import modules.services as Services
import modules.products as Products
import modules.sales as Sales
import modules.reports as Reports

base_path = os.path.dirname(__file__)

def menu_users():
    print("+++ Modulo de Usuarios +++")
    print ()
    # Read Users
    users = Users.read(base_path, "/DB/users.json")
    # Mostrar usuarios existentes
    Tables.create_table(1, users, CONSTANTS.HEADERS_USERS)
    
    print()
    print("1. Crear | 2. Actualizar | 3. Eliminar")
    print()
    op_user = input("Seleccione la accion:\n --> ")
    print()
    
    if op_user == "1":
        Users.create(base_path, users)
    
    if op_user == "2":
        print()
        id = input("Digite el ID del usuario que desea actualizar:\n --> ")
        Users.update(base_path, users, id)
    
    if op_user == "3":
        print()
        id = int(input("Digite el Id del usuario que desea eliminar:\n --> "))
        Users.delete(base_path, users, id)

def menu_services():
    op_services = input("Seleccionar el Servicio:\n1. Planes | 2. Fibra Optica\n --> ")
    print()
    
    if op_services == "1":
        #Read Services
        services_plans = Services.read(base_path, "/DB/services_plans.json")
        # Mostrar planes existentes
        Tables.create_table(1, services_plans, CONSTANTS.HEADERS_PLANS)
    
    if op_services == "2":
        #Read Services
        services_fiber = Services.read(base_path, "/DB/services_fiber.json")
        # Mostrar fibra existentes
        Tables.create_table(1, services_fiber, CONSTANTS.HEADERS_FIBER)
    
    print()
    print("1. Crear | 2. Actualizar | 3. Eliminar")
    print()

    op_action = input("Seleccione la acción que desee realizar: \n --> ")
    
    if op_action == "1":
        if op_services == "1":
            Services.create(base_path, services_plans, None)
        if op_services == "2":
            Services.create(base_path, None, services_fiber) 

    if op_action == "2":
        if op_services == "1":
            id = input("Digite el ID del plan que desea actualizar:\n --> ")
            Services.update(base_path, id, services_plans, None)
        if op_services == "2":
            id = input("Digite el ID de la fibra óptica que desea actualizar:\n --> ")
            Services.update(base_path, id, None, services_fiber)
    
    if op_action == "3":
        if op_services == "1":
            print()
            id = int(input("Digite el Id del plan que desea eliminar:\n --> "))
            Services.delete(base_path, id, services_plans, None)
        if op_services == "2":
            id = int(input("Digite el Id de la fibra óptica que desea eliminar:\n --> "))
            Services.delete(base_path, id, None, services_fiber)

def menu_products():
    #Read Products
    products = Crud.read_db(base_path, "/DB/products.json")
    Tables.create_table(1, products, CONSTANTS.HEADERS_PRODUCTS)
    
    print()
    print("1. Crear | 2. Actualizar | 3. Eliminar")
    print()
    op_product = input("Seleccione la accion:\n --> ")
    print()
    
    if op_product == "1":
        Products.create(base_path, products)
        
    if op_product == "2":
        print()
        id = input("Digite el ID del producto que desea actualizar:\n --> ")
        Products.update(base_path, products, id)

    if op_product == "3":
        print()
        id = int(input("Digite el Id del producto que desea eliminar:\n --> "))
        Products.delete(base_path, products, id)

def menu_sales():
    sales = Sales.read(base_path, "/DB/sales.json")
    op_sales = input("1. Servicios | 2. Productos:\n")
    
    if op_sales == "1":
        op_sales_services = input("1. Planes | 2. Internet:\n")
        
        if op_sales_services == "1":
            #Read Services
            services_plans = Services.read(base_path, "/DB/services_plans.json")
            # Mostrar planes existentes
            Tables.create_table(1, services_plans, CONSTANTS.HEADERS_PLANS)
            
            op_action = input("1. Vender | 0. Salir: \n")
            if op_action == "1":
                print("Create Sale")
                id_sale_prod = input("Digite el ID del plan que desea vender:\n")
                Sales.create(base_path, sales, services_plans, 1, id_sale_prod, "plan") 
        
        if op_sales_services == "2":
            #Read Services
            services_fiber = Services.read(base_path, "/DB/services_fiber.json")
            # Mostrar fibra existentes
            Tables.create_table(1, services_fiber, CONSTANTS.HEADERS_FIBER)
            
            op_action = input("1. Vender | 0. Salir: \n")
            if op_action == "1":
                print("Create Sale")
                id_sale_prod = input("Digite el ID del internet que desea vender:\n")
                Sales.create(base_path, sales, services_fiber, 1, id_sale_prod, "optical_fiber") 
        
    if op_sales == "2":
        # Read Products
        products = Crud.read_db(base_path, "/DB/products.json")
        
        available_products = []
        
        for prd in products:
            if prd['stock'] > 0:
                available_products.append(prd)
        
        Tables.create_table(1, available_products, CONSTANTS.HEADERS_PRODUCTS)
        
        op_action = input("1. Vender | 0. Salir: \n")
        if op_action == "1":
            print("Create Sale")
            id_sale_prod = input("Digite el ID del producto que desea vender:\n")
            Sales.create(base_path, sales, available_products, 2, id_sale_prod, "product") 
        
def menu_reports():
    sales = Sales.read(base_path, "/DB/sales.json")
    # Read services
    services_plans = Services.read(base_path, "/DB/services_plans.json")
    services_fiber = Services.read(base_path, "/DB/services_fiber.json")
    products = Products.read(base_path, "/DB/products.json")
    # Informes cantidad de productos | servicios
    op_report = input("1. Productos/Servicios | 2. Servicios Populares | 3. Informe Usuario/ProductoServicio:\n")
    
    if op_report == "1":
        print()
        print()
        Reports.company_ps(products, services_plans, services_fiber)
        
    if op_report == "2":
        Reports.popular_services(sales, services_plans, services_fiber)
        
    if op_report == "3":
        users = Users.read(base_path, "/DB/users.json")
        Reports.users_services_products(sales, users, services_plans, services_fiber, products)

def menu():
    print()
    print("*******************************************************************")
    print()
    print("***** Bienvenido al Sistema de Claro *****")
    print()
    print("Seleccionar a donde desea ingresar: |->")
    print()
    print("1. Usuarios | 2. Servicios | 3. Productos | 4. Ventas | 5. Reportes")
    print()
    op_mod = input("Seleccione el modulo:\n --> ")
    print(op_mod)
    
    if op_mod == "1":
        menu_users()
    
    if op_mod == "2":
        print()
        print("+++ Servicios +++")
        print()
        menu_services()
        
    if op_mod == "3":
        print()
        print("+++ Productos +++")
        print()
        menu_products()
    
    if op_mod == "4":
        print()
        print("+++ Ventas +++")
        print()
        menu_sales()
        
    if op_mod == "5":
        print()
        print("+++ Reportes +++")
        print()
        menu_reports()

def main():
    print(base_path)
    menu()
    
    os.system("pause")

if __name__ == '__main__':
    main()