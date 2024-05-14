import modules.crud as Crud
import modules.tool_tabulate as Tables
import constants.contants as CONSTANTS

def read(base_path, path_db):
    users = Crud.read_db(base_path, path_db)
    return users

def create(base_path, users):
    # Determina el id consecutivo del usuario a crear
    max_id = 0
    for usr in users:
        id_current = usr.get("id", 0)
        max_id = max(max_id, id_current)
    
    max_id += 1
    new_user = {
        "id": max_id,
        "name": "",
        "num_document": 0,
        "address": "",
        "phone": 0,
        "email": "",
        "rol": "",
        "type_client": ""
    }
    print()
    print("**** Creación de Usuario N: "+ str(max_id) +" ****")
    print()
    new_user['name'] = input("Digite el nombre:\n --> ")
    print()
    new_user['num_document'] = input("Digite el número de documento: \n --> ")
    print()
    new_user['address'] = input("Digite la dirección: \n --> ")
    print()
    new_user['phone'] = input("Digite el número telefónico: \n --> ")
    print()
    new_user['email'] = input("Digite el correo electrónico: \n --> ")
    print()

    print ("Seleccione el rol: ")
    print()
    op_rol = input("1. Admin | 2. Cliente: \n --> ")
    print()
    if op_rol == "1":
         new_user['rol'] = "admin"
    if op_rol == "2":
        new_user['rol'] = "client"
        op_client = input("1. Cliente Nuevo | 2. Cliente Regular | 3. Cliente Leal: \n --> ")
        print()
        if op_client == "1":
            new_user['type_client'] = "new client"
        if op_client == "2":
            new_user['type_client'] = "regular client"
        if op_client == "3":
            new_user['type_client'] = "real client"

    Crud.create(base_path, "/DB/users.json", users, new_user, "El usuario ha sido creado exitosamente")
    return new_user['id']

def update(base_path, users, id):
    
    for usr in users:
        if usr['id'] == int(id):
            Tables.create_table(2, usr, CONSTANTS.HEADERS_USERS)
            op_field = 99
            
            while op_field != 0:
                print()
                op_field = input( "Seleccione el campo del usuario que desea actualizar:\n" +
                    "1. Nombre | 2. Documento | 3. Direccion | 4. Telefono | 5. Email | 6. Rol | 7. Tipo de Cliente | 0. Salir del usuario\n -->"
                    )
                print()

                if op_field == "1":
                    name = input("Digite el nombre:\n --> ")
                    print()
                    usr['name'] = name
                if op_field == "2":
                    num_document = input("Digite el número de documento:\n --> ")
                    print()
                    usr['num_document'] = num_document
                if op_field == "3":
                    address = input("Digite la dirección:\n --> ")
                    print()
                    usr['address'] == address
                if op_field == "4":
                    phone = input("Digite el número de teléfono:\n --> ")
                    print()
                    usr['phone'] = phone
                if op_field == "5":
                    email = input("Digite el correo electrónico:\n --> ")
                    print()
                    usr['email'] = email
                if op_field == "6":
                    rol = input("Digite el rol que desee:\n --> ")
                    print()
                    if rol == "1":
                        usr['rol'] = "admin"
                    if rol == "2":
                        usr['rol'] = "client"
                        if op_field == "7":
                            type_client =(input("Seleccione 1. Cliente Nuevo | 2. Cliente Regular | 3. Cliente Leal\n --> "))
                            print()
                            if type_client == "1":
                                usr['type_client'] = "new client"
                            if type_client == "2":
                                usr['type_client'] = "regular client"
                            if type_client == "3":
                                usr['type_client'] = "leal client"
                if op_field == "0":
                    break
                Crud.update(base_path, "/DB/users.json", users, "El usuario ha sido actualizado exitosamente")
    
def delete(base_path, users, id):
    Crud.delete(base_path, "/DB/users.json", users, id, "El usuario ha sido eliminado exitosamente")
       
            
        
        
        
        
    
    