my_name = 'albert kong'
my_age = 32 # sad but true
my_height_inches = 70 #inches
my_height_cm = my_height_inches * 2.54 #centimeter
my_weight = 70 #KG
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'


print(f"Let's talk about {my_name}.")
print(f"He's {my_height_inches} inches tall.")
print(f"He's {my_height_cm} cm tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually that's not to heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height_cm +my_weight
print(f"If i add {my_age}, {my_height_cm}, and {my_weight} I get {total}.")
