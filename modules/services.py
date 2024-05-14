import modules.crud as Crud
import modules.tool_tabulate as Tables
import constants.contants as CONSTANTS

def __id_consecutive(data):
    max_id = 0
    for serv in data:
        id_current = serv.get("id", 0)
        max_id = max(max_id, id_current)
    return max_id

def read(base_path, path_db):
    services = Crud.read_db(base_path, path_db)
    return services

def create(base_path, plans = None, optical_fiber = None):
    if plans != None:
        # Determina el id consecutivo del plan a crear 
        max_id = __id_consecutive(plans)
        max_id +=1
        new_plan = {
        "id": max_id,
        "name": "",
        "type_plan": 0,
        "fixed_charge": "",
        "cuantity_days": 0
        }
        print("**** Creación de Planes N: "+ str(max_id) +" ****")
        print()
        new_plan['name'] = input("Digite el nombre:\n --> ")
        print()
        new_plan['type_plan'] = input("Digite el tipo de plan: \n --> ")
        print()
        new_plan['fixed_charge'] = input("Digite el cargo fijo: \n --> ")
        print()
        new_plan['cuantity_days'] = input("Digite la cantidad de días: \n --> ")
        print()
        Crud.create(base_path, "/DB/services_plans.json", plans, new_plan, "El servicio de plan ha sido creado exitosamente")
    

    if optical_fiber != None:
        # Determina el id consecutivo de la fibra óptica a crear 
        max_id = __id_consecutive(optical_fiber)
        max_id +=1
        new_optical_fiber = {
        "id": max_id,
        "name": "",
        "price": 0,
        "capacity": ""
        }
        print("**** Creación de Fibra Óptica N: "+ str(max_id) +" ****")
        print()
        new_optical_fiber['name'] = input("Digite el nombre:\n --> ")
        print()
        new_optical_fiber['price'] = input("Digite el precio: \n --> ")
        print()
        new_optical_fiber['capacity'] = input("Digite la capacidad: \n --> ")
        print()
        Crud.create(base_path, "/DB/services_fiber.json", optical_fiber, new_optical_fiber, "El servicio de fibra optica ha sido creado exitosamente")

def update (base_path, id, plans = None, optical_fiber = None):
    if plans != None:
        for plan in plans: 
            if plan['id'] == int(id):
                Tables.create_table(2, plan, CONSTANTS.HEADERS_PLANS)
                op_field = 99
                
                while op_field != 0:
                    print()
                    op_field = input("Seleccione el campo del servicio que desea actualizar: \n" +
                    "1. Nombre | 2. Tipo de Plan | 3. Cargo Fijo | 4. Cantidad de Días | 0. Salir de Planes \n --> ")
                    print()
        
                    if op_field == "1":
                        name = input("Digite el nombre:\n --> ")
                        print()
                        plan['name'] = name
                    if op_field == "2":
                        type_plan = input("Digite el tipo de plan:\n --> ")
                        print()
                        plan['type_plan'] = type_plan
                    if op_field == "3":
                        fixed_charge = input("Digite el cargo fijo:\n --> ")
                        print()
                        plan['fixed_charge'] = int(fixed_charge)
                    if op_field == "4":
                        cuantity_days = input("Digite la cantidad de días:\n --> ")
                        print()
                        plan['cuantity_days'] = int(cuantity_days)
                    if op_field == "0":
                        break
                    
                    Crud.update(base_path, "/DB/services_plans.json", plans, "El servicio de planes ha sido actualizado exitosamente")    
    
    if optical_fiber != None:
        for optical_fib in optical_fiber:
            if optical_fib['id'] == int(id):
                Tables.create_table(2, optical_fib, CONSTANTS.HEADERS_FIBER)
                op_field = 99
            
                while op_field != 0:
                    print()
                    op_field = input("Seleccione el campo del servicio que desea actualizar:\n" +
                    "1. Nombre | 2. Precio | 3. Capacidad | 0. Salir de Fibra óptica: \n --> ")
                    print()
                    if op_field == "1":
                        name = input("Digite el nombre:\n --> ")
                        print()
                        optical_fib['name'] = name
                    if op_field == "2":
                        price = input("Digite el precio correspondiente:\n --> ")
                        print()
                        optical_fib['price'] = float(price)
                    if op_field == "3":
                        capacity = input("Digite la capacidad:\n --> ")
                        print()
                        optical_fib['capacity'] = capacity
                    if op_field == "0":
                        break
                
                    Crud.update(base_path, "/DB/services_fiber.json", optical_fiber, "El servicio de fibra óptica ha sido actualizado exitosamente")
                    
def delete (base_path, id, plans = None, optical_fiber = None):
    
    if plans != None:
        Crud.delete(base_path, "/DB/services_plans.json", plans, id, "El servicio de planes ha sido eliminado exitosamente")
    
    if optical_fiber != None: 
        Crud.delete(base_path, "/DB/services_fiber.json", optical_fiber, id, "El servicio de fibra óptica ha sido eliminado exitosamente")       
    
    
                
                
    
            
    
        
    
    
    