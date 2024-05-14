import os
import json

def read_db(base_path, path_db):
    with open(base_path + path_db, 'r') as db:
        data = db.read()
        obj_json = json.loads(data)
        return obj_json
    
def create(base_path, path_db, obj_data, new_data, message):
    # Agregamos el nuevo objeto a la DB existente
    obj_data.append(new_data)
    with open(base_path + path_db, 'w') as data:
        json.dump(obj_data, data, indent=4)
        print(message)
        
def update(base_path, path_db, obj_data, message): 
    with open(base_path + path_db, 'w') as data:
        json.dump(obj_data, data, indent=4)
        print(message)
        
def delete(base_path, path_db, obj_data, id, message):
    # Se busca el registro
    for obj in obj_data:
        if obj["id"] == id:
            obj_data.remove(obj)
            break
    
    with open(base_path + path_db, 'w') as data:
        json.dump(obj_data, data, indent=4)
        print(message)
    