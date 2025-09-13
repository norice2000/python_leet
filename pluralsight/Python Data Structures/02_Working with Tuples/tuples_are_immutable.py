# Creating tuples
empty_tuple = ()
print(empty_tuple)

# Tuple with coma
one_element_tuple = (32, )
print(one_element_tuple)

# Mutiple of elements
multi_element_tuple = (1, "apply", 3.14)
print(multi_element_tuple)

# Tuple without paranthesis
implicit_tuple = 10, 20, 30
print(implicit_tuple)

## Accessing Tuple Elements
rgb = (150, 100, 200)

print(f"Accessing middle tuple: {rgb[1]}")
print(f"Accessing last tuple with rbg[-1]: {rgb[-1]}")