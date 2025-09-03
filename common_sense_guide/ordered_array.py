def linear_search(array, search_value):
    for index, element in enumerate(array):
        print(f"index: {index}, element: {element}, search_value: {search_value}")
        if element == search_value:
            return index
        elif element > search_value:
            break # it will stop searching if value is more than 22

    return None

array_list = set(sorted([3,202,75,80,202]))

# using set, makes sure it is unique but turns it into a tuple

print(f"sorted: {str(array_list)}")
# print(linear_search(array_sorted, 22))