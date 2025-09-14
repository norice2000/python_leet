# Creating Dictionary view objects with `items()` which gives it a list and tuples format output
prices = {
    "keyboard": 30,
    "mouse": 10,
    "monitor": 80
}

print(prices.items())
# output: dict_items([('keyboard', 30), ('mouse', 10), ('monitor', 80)])

# Sorting Dictionary Key
# default is that it will sort by the first element (in this case keyboard, mouse monitor)
sorted_alpha = sorted(prices.items()) # this will sort it as a list with tuples
print(f"sorted_alpha: {sorted_alpha}")

conv_dict = dict(sorted_alpha)
print(f"conv_dict: {conv_dict}")

# Sorting by Dict Value, use the lambda
sorted_prices = dict(sorted(prices.items(), key=lambda x: x[1]))
print(sorted_prices)

# Alternative to sorting by dictValue
from operator import itemgetter

sorted_prices_getter = dict(sorted(prices.items(), key=itemgetter(1)))
print(sorted_prices_getter)