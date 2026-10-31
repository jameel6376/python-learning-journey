menu_items = tuple(('Espresso', 'Latte', 'Pastry'))
customer_order = []

shop_name = 'pythonic brew cafe'
shop_name = (shop_name.upper())
print('=' * 50)
print(shop_name.center(50))
print('=' *50)
print( f'{menu_items[0]}\n{menu_items[1]}\n{menu_items[2]}')

total_budget = (input('What is your total budget in cash?\n'))
form_total = int(total_budget)

espressos = form_total // 4
fact = (f'You can afford up to {espressos:.0f} Espressos!')

if espressos == 0:
    pass
else:
    print(fact)

choice = (input('pick your first item\n'))
if choice == 'Espresso':
    customer_order.append(menu_items[0])
elif choice == 'Latte':
    customer_order.append(menu_items[1])
elif choice == 'Pastry':
    customer_order.append(menu_items[2])
else:
    print('error')
    customer_order.append('Water')

choice2 = (input('pick your second item\n'))
if choice2 == 'Espresso':
    customer_order.append(menu_items[0])
elif choice2 == 'Latte':
    customer_order.append(menu_items[1])
elif choice2 == 'Pastry':
    customer_order.append(menu_items[2])
else:
    print('error')
    customer_order.append('Water')

cart = len(customer_order)
print(f'You have {cart:.0f} items in your cart.')

total_bill = 0

if customer_order[0] == 'Espresso':
    total_bill += 4
    
elif customer_order[0] == 'Latte':
    total_bill += 6
    
elif customer_order[0] == 'Pastry':
    total_bill += 5



if customer_order[1] == 'Espresso':
    total_bill += 4
    
elif customer_order[1] == 'Latte':
    total_bill += 6
    
elif customer_order[1] == 'Pastry':
    total_bill += 5

customer_order.sort()

item1= customer_order[0]
item2 = customer_order[1]

total_budget = int(total_budget)
change = total_budget - total_bill




ecost = 4
latte = 6
pastry = 5
water = 0
bill = 0
bill2 = 0

if  item1 == 'Espresso':
    bill = ecost
elif  item1 == 'Latte':
    bill = latte
elif  item1 == 'Pastry':
    bill = pastry

if  item2 == 'Espresso':
    bill2 = ecost
elif  item2 == 'Latte':
    bill2 = latte
elif  item2 == 'Pastry':
    bill2 = pastry

moneyleft = 0
if total_budget >= total_bill:
    change = total_budget - total_bill
    change = str(change)
    bill = str(bill)
    bill2 = str(bill2)
    total_bill = str(total_bill)
    print(item1.ljust(20, '.') + bill.rjust(10, '.'))
    print(item2.ljust(20, '.') + bill2.rjust(10, '.'))
    print ('Change'.ljust(20, '.') + change.rjust(10, '.'))
    print ('Total bill'.ljust(20, '.') + total_bill.rjust(10, '.'))

else:
     moneyleft = total_bill - total_budget
     print(f'not enough cash, ${moneyleft} short')





      

