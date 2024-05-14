from tabulate import tabulate

def create_table(op_table, all_data, headers):
    data = []
    
    if op_table == 1:
        fields = list(all_data[0].keys())
        for usr in all_data:
            row = [usr[field] for field in fields]
            data.append(row)
        
    if op_table == 2:
        fields = list(all_data.keys())        
        row = [all_data[field] for field in fields]
        data.append(row)
        
    # Mostrar datos existentes
    print(tabulate(data, headers=headers, tablefmt="rounded_grid"))