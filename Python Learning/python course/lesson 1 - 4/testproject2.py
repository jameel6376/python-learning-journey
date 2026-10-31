cargo_item = ("uranium crystals")
weight_string = ("450.8")
weight_string = (float(weight_string))
shielding_weight = weight_string * 0.12
total_weight = (shielding_weight + weight_string)
cargo_item = (cargo_item.title())
form_cargo = f"{weight_string:.1f} kg"
form_shielding = f"{shielding_weight:.1f} kg"
form_total = f"{total_weight:.1f} kg"
print(cargo_item.ljust(23, ".") + form_cargo.rjust(12, "."))
print("Shielding Weight".ljust(23, ".") + form_shielding.rjust(12, "."))
print("Total Weight".ljust(23, ".") + form_total.rjust(12, "."))



