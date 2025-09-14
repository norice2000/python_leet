books = {
    "book_1": "cookbook",
    "book_2": "buffBaby",
    "book_3": "linuxbook"
}

# use `del`
# print(f"prior to remove: {books}")
# del books['book_2']
# print(f"books: {books}")

# using pop will delete, and retain its value
print(f"books: {books}")
pop_value = books.pop('book_3')
print(f"popped value: {pop_value}")
print(f"after pop: {books}")


# using pop() to signify something doesnt exists
sensor = {
    "temp": "22C"
}

# if the default value is not provided for a non-existent keys, pop() will raise a KeyError
value = sensor.pop("pressure", "Pressure is not found") #this raises a default value if it does not exist
print(value)

# Great for LIFO data structure, or a cache
# Removing items with `popitem()` where it removes the last item
equips = {
    "item_1": "sword",
    "item_2": "shield",
    "item_3": "staff"
}
print(f"prior to pop: {equips}")

# remove last item which is item_3 staff
last_element = equips.popitem()

print(f"Pop item: {last_element}")
print(f"current: equips: {equips}")

# can use <dict>.clear() this will remove all items