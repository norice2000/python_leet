# Configurations cannot skip a number in the ordering. 
# If there are three configuration strings, there must be a 1, 2, and 3 index

# in this case we need to create a tuple () data type inside a list data type [ ]

pizza_order = ("Large", "Pepperoni") # tuple
print(f"Pizza order: {pizza_order}")
print(f"0 index tuple: {pizza_order[0]}") # prints Large
print(f"1 index tuple: {pizza_order[1]}") # prints Pepperoni

# Anotehr example of a person in tuples
dog_info = ("Champ", "Dog", 12)

print(f"Name: {dog_info[0]}, Animal: {dog_info[1]}, Age: {dog_info[2]}") # prints Name: Champ, Animal: Dog, Age: 12


# unpacking a tuple to respective variables
size, toppings = pizza_order
print(f" Size: {size}, Toppings: {toppings}")

