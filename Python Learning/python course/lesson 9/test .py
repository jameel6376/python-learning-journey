
def calculate_item_price(item_type, quantity):
    if item_type == 'coffee':
        base_price = 3.50
    elif item_type == 'tea':
        base_price = 2.50
    elif item_type == 'muffin':
        base_price = 4.00
    else:
        base_price = 0.00
    total_cost = base_price * quantity
    return total_cost

grand_total = 0.0
items = {'tea', 'coffee', 'muffin'}

while True:
    userinput = input('what would you like to order? \n').strip().lower()
    if userinput in items:
        quant = int(input('how many would you like? \n'))
        total = calculate_item_price(userinput, quant)
        total = calculate_item_price(userinput, quant)
        grand_total = total + grand_total
    if userinput == 'checkout':
        break  #emergency exit
message = 'goodbye'
print(f"your total cost is {grand_total}")
print('*' * 20)
print(message.center(20, '*'))
print('*' * 20)





# # Use a dictionary to store items and their prices (Much cleaner!)
# MENU = {
#     'coffee': 3.50,
#     'tea': 2.50,
#     'muffin': 4.00
# }

# def calculate_item_price(item_type, quantity):
#     # Look up the price in the dictionary. Default to 0.00 if not found.
#     base_price = MENU.get(item_type, 0.00)
#     return base_price * quantity

# grand_total = 0.0

# while True:
#     userinput = input('What would you like to order? (Type "checkout" to finish) \n').strip().lower()
    
#     if userinput == 'checkout':
#         break
        
#     if userinput in MENU:
#         try:
#             quant = int(input('How many would you like? \n'))
#             total = calculate_item_price(userinput, quant)
#             grand_total += total  # Shorthand for grand_total = grand_total + total
#         except ValueError:
#             print("Please enter a valid number for quantity!")
#     else:
#         print("Sorry, we don't serve that item. Try again.")

# # Final receipt formatting
# print('\n' + '*' * 20)
# print(f"Your total cost is ${grand_total:.2f}") # Formats to 2 decimal places
# print('*' * 20)
# print('goodbye'.center(20, '*'))
# print('*' * 20)










    



    






    





 

