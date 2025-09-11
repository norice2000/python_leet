letters = ["a", "b", "c", "d", "e", "f", "g"]

# List [start:end:step] (get every other element)
print(f"slicing: {letters[1:6:2]}")

# reverse
print(f"reverse slice: {letters[::-1]}")



current_list = ["hello", "world", "people"]

print(f" current list: {current_list}")
# copy the current list as new list
new_list = list(current_list)
#appending new list to demonstrate this
new_list.append("appended")
print(f" new list: {new_list}")

# current list: ['hello', 'world', 'people']
#  new list: ['hello', 'world', 'people', 'appended']


import copy
# Shallow Copy of a Nest List
settings = [["volume", 70], ["brightness", 50]]

shallow_copy = list(settings)
shallow_deepcopy = copy.deepcopy(settings)

# modify inner list in the shallow copy
print(f"Before: {shallow_copy}")
shallow_copy[0][1] = 20
shallow_deepcopy[1][1] = 30

print(f"Oringinal: {settings}")
print(f"shallow: {shallow_copy}")
print(f"Deepcopy: {shallow_deepcopy}")
# output issue below where it modifes the same one
# Oringinal: [['volume', 20], ['brightness', 50]]
# shallow: [['volume', 20], ['brightness', 50]]
# Deepcopy: [['volume', 70], ['brightness', 30]]
#FIXED by using deepcopy
# import copy