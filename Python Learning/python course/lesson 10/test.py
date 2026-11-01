#terminal-based grade and inventory management system
inventory = {
    'notebooks': 15,
    'pens': 30,
    'erasers': 22
}

def update_stock(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def calculate_total_items(quantities_list):
    if len(quantities_list) == 0:
        return 0
    return quantities_list[0] + calculate_total_items(quantities_list[1:])

while True:
    gui = input('\n1:View Inventory and Total items \n2:Add/Update Item Stock \n3:Exit Program \n')
    if gui not in ['1', '2', '3']:
        print('invalid choice: try again.')
        continue
    elif gui == '1':
        for item, quantity in inventory.items():
            print(item + ' ' + str(quantity))
            total = calculate_total_items(list(inventory.values()))
        print(f'total items in inventory {total}')
    elif gui == '2':
        itname = input('enter item name:\n')
        itquant = int(input('enter quantity: \n'))
        upstock = update_stock(itname, itquant)
        print(f'stock updated!\n item:{itname}\n quantity: {itquant}\n')
    elif gui == '3':
        print('goodbye!')
        break
    else:
        print('invalid option! try again')
        continue

def update_stock(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def calculate_total_items(quantities_list):
    if len(quantities_list) == 0:
        return 0
    return quantities_list[0] + calculate_total_items(quantities_list[1:])

while True:
    gui = input('\n1:View Inventory and Total items \n2:Add/Update Item Stock \n3:Exit Program \n')
    if gui not in ['1', '2', '3']:
        print('invalid choice: try again.')
        continue
    elif gui == '1':
        for item, quantity in inventory.items():
            print(item + ' ' + str(quantity))
        total = calculate_total_items(list(inventory.values()))
        print(f'total items in inventory {total}')
    elif gui == '2':
        itname = input('enter item name:\n')
        itquant = int(input('enter quantity: \n'))
        upstock = update_stock(itname, itquant)
        print(f'stock updated!\n item:{itname}\n quantity: {itquant}\n')
    elif gui == '3':
        print('goodbye!') 
        break  
    else:
        print('invalid option! try again')
        








        