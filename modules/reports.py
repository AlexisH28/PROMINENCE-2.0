import modules.tool_tabulate as Tables
import constants.contants as CONSTANTS
from collections import Counter

def most_sale(sales_data):
    keys = [key for s_data in sales_data for key in s_data.keys()]
    count_keys = Counter(keys)
    return count_keys.most_common(1)[0][0]

def get_most_sale(data, id):
    for dt in data:
        if dt['id'] == id:
            return dt

def company_ps(products, services_plans, services_fiber):
    print("***** Informes sobre cantidad de productos/servicios: *****")
    print("** Tabla de Productos **")
    Tables.create_table(1, products, CONSTANTS.HEADERS_PRODUCTS)
    print()
    print("**Tabla de Servicios/Planes **")
    Tables.create_table(1, services_plans, CONSTANTS.HEADERS_PLANS)
    print()
    print("**Tabla de Servicios/Internet **")
    Tables.create_table(1, services_fiber, CONSTANTS.HEADERS_FIBER)

def popular_services(sales, services_plans, services_fiber):
    sales_plan = []
    sales_fiber = []
    
    # Se recorren las ventas para luego separarlas por tipo de servicio/producto
    # y se guardan como objeto en un array {"id_ps": cuantity}
    for sale in sales:
        if sale['type_ps'] == "plan":
            sales_plan.append({sale["id_ps"]: sale["cuantity"]})
        elif sale['type_ps'] == "optical_fiber":
            sales_fiber.append({sale["id_ps"]: sale["cuantity"]})
    
    # Se obtiene el id de cada mas vendido
    id_most_sale_plan = most_sale(sales_plan)
    id_most_sale_fiber = most_sale(sales_fiber)
    
    most_sale_plan = []
    most_sale_fiber = []
    
    # Se obtiene el servicio mas vendido con todos sus datos
    most_sale_plan.append(get_most_sale(services_plans, id_most_sale_plan))
    most_sale_fiber.append(get_most_sale(services_fiber, id_most_sale_fiber))
    
    print("** Tabla de Servicios Mas Populares **")
    print()
    print("* Planes *")
    Tables.create_table(1, most_sale_plan, CONSTANTS.HEADERS_PLANS)
    print()
    print("* Internet *")
    Tables.create_table(1, most_sale_fiber, CONSTANTS.HEADERS_FIBER)

def users_services_products(sales, users, services_plans, services_fiber, products):
    # Obtener los id product/service que se han vendido
    # Se recorren las ventas para luego separarlas por tipo de servicio/producto
    # y se guardan como objeto en un array {"id_ps": cuantity}
    sales_services = []
    for sale in sales:
        if sale['type_ps'] == "plan":
            user_plan = [usr for usr in users if usr['id'] == sale['id_user']]
            srv_plan = [srv for srv in services_plans if srv['id'] == sale['id_ps']]
            sales_services.append({"name": user_plan[0]['name'], "email": user_plan[0]['email'], "name_ps": srv_plan[0]['name'], "price": sale['price_sale'], "cuantity": 0})
        elif sale['type_ps'] == "optical_fiber":
            user_fiber = [usr for usr in users if usr['id'] == sale['id_user']]
            srv_fiber = [srv for srv in services_fiber if srv['id'] == sale['id_ps']]
            sales_services.append({"name": user_fiber[0]['name'], "email": user_fiber[0]['email'], "name_ps": srv_fiber[0]['name'], "price": sale['price_sale'], "cuantity": 0})
        elif sale['type_ps'] == "product":
            user_prd = [usr for usr in users if usr['id'] == sale['id_user']]
            product = [prd for prd in products if prd['id'] == sale['id_ps']]
            sales_services.append({"name": user_prd[0]['name'], "email": user_prd[0]['email'], "name_ps": product[0]['name'], "price": sale['price_sale'], "cuantity": sale['cuantity']})
    
    if sales_services != []:
        print("** Informe Usuarios - Servicios/Productos **")
        print()
        Tables.create_table(1, sales_services, CONSTANTS.HEADERS_INFO_USER_PS)
    else:
        print("----- No hay ventas para mostrar el informe -----")