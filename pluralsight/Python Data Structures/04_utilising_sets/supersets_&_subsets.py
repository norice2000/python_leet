# `issubset()` gives True if the set1 does have the same value inside set2
set1 = {1, 2}
set2 = {1, 2, 3, 4, 5}

print(set1.issubset(set2)) # output: True


ingredients_at_home = {"flour", "sugar", "egg"}
pancake_ingredients = {"flour", "egg"}

print(pancake_ingredients.issubset(ingredients_at_home))

#issupersets, check if a set Contains ALL elements of Another set
my_tools = {"hammer", "screwdriver", "pliers"}
chair_tools = {"hammer", "screwdriver"}

print(f"Does my tools suffice to build a chair? {my_tools.issuperset(chair_tools)}") # True

#improper sets are when both sets are equal

#Check if Two sets have no elements in common with `isdisjoint()`
allergens = {"peanuts", "gluten", "soy", "dairy"}

choco_ingredients = {"coco", "sugar", "dairy"}

fruit_salad_ingredients = {"apple", "banana"}

print(f"isdisjoint to see if it contains allergens: {allergens.isdisjoint(choco_ingredients)}") # Returns False since it contains it