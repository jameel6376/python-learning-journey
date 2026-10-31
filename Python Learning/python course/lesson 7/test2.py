correct_pin = "1234"
account_balance = (float(500))
user  = input("Enter your username \n")
username = (user.strip()).lower()
pin = input("enter your pin: \n")

if pin == correct_pin:
    print("access granted")
else:
    print("denied:invalid pin")
    exit()

withdrawal_amount = float(input("How much money would you like to withdraw? \n"))

if withdrawal_amount <= account_balance:
    sub = account_balance - withdrawal_amount
    print(f"new account balance is {sub} ")
else:
    print("Error: insufficient funds")






   