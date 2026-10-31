from enum import Enum
class Faction(Enum):
    CITIZEN = 1
    BOUNTY_HUNTER = 2
    PIRATE = 3

pilot_name = (input("What is your space pilot name?"))
product = (input('what product are you buying?'))
faction = (input("what is your faction number? \n 1, 2 or 3?"))
faction = int(faction)
base_price = ("250.00")
base_price = (float(base_price))
total = 0
phrase1 = 'Welcome, Trader.'
phrase2 = "Weapons logged."
phrase3 = "GUARD ESCORT ACTIVE!"
phrase4 = 'Unknown entity.'
final_phrase = 0
if faction == 1:
    final_phrase = (phrase1)
    total = (base_price * 0.10 + base_price)
elif faction == 2:
    final_phrase = (phrase2)
    total = (base_price * 0.20 + base_price)
elif faction == 3:
    final_phrase = (phrase3)
    total = (base_price * 0.00 + base_price)
else:
    final_phrase = (phrase4)
    total = (base_price)

form_product = product.replace("_", " ").title()
form_pilot = pilot_name.strip().upper()

print ("=" * 38)
print(final_phrase.center(38))
print(form_pilot.ljust(26) + str(Faction(faction)).rjust(12).replace("Faction.", ""))
print(form_product.ljust(26, ".") + (f"${total:.2f}").rjust(12))


    




