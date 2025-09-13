steps = ("start", "load data", "process", "validate", "save", "end")

# Two ways to reverse a tuple since they are immutable

#reversed
reverse_steps = tuple(reversed(steps)) #this recreates a tuple, PREFERRED since it is lazy loading data
print(reverse_steps)
# output: ('end', 'save', 'validate', 'process', 'load data', 'start')

#slicing
reverse_steps_slice = reverse_steps[::-1]
print(reverse_steps_slice)
# output: ('start', 'load data', 'process', 'validate', 'save', 'end')

# sorting
values = (1, 3, 2)
sort_tuple = tuple(sorted(values))
print(sort_tuple)
# (1, 2, 3)

#sorting tuples with the key argument
records = (
    ("sensor1", 30),
    ("sensor2", 25),
    ("sensor3", 40),
)

sorted_by_value = tuple(sorted(records, key=lambda x: x[1]))
print(f"Sorted with lamnda for tuple: {sorted_by_value}")

# output
# Sorted with lamnda for tuple: (('sensor2', 25), ('sensor1', 30), ('sensor3', 40))

products = (
    ("product_a", 120, 10),
    ("product_b", 200,100),
    ("product_c", 150,20),
) # (name, price, discount_price)

sorted_by_final_price = tuple(sorted(products, key=lambda x: x[1] - x[2]))
print(f"Sorted final price: {sorted_by_final_price}")
#Sorted final price: (('product_b', 200, 100), ('product_a', 120, 10), ('product_c', 150, 20))