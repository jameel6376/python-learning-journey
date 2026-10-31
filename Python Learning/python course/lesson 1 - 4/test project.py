product = ("Neon_Burger")
cost_string = (str(15.00))
cost_string = (float(cost_string))
tip = (cost_string * 0.15)
total_bill = (cost_string + tip)
product =(product.replace("_", " "))
product =(product.title())
form_price= f"${cost_string:.2f}"
form_tip=f"${tip:.2f}"
form_total=f"{total_bill:.2f}"
print(product.ljust(20, ".") + form_price.rjust(10))
print("tip (15%)".ljust(20) + form_tip.rjust(10))
print("Total Due".ljust(20) + form_total.rjust(10))

