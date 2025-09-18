my_array = [7, 12, 9, 4, 11, 8]
minVal = my_array[0]

# my_array.sort()
# minVal = my_array[0]
# print(my_array)
# print(minVal)


for i in my_array:
    if i < minVal:
        minVal = i

print(f"Lowest value: {minVal}")