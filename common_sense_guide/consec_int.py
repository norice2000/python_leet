array1 = [1,2,3]
array2 = [2,3,5]


def consec_int(array: list):
    array.sort()
    start = array[0]
    expect = list(range(start, start + len(array)))
    print(f"expect: {expect}, start: {start}, increment with start + {len(array)}")

    if expect == array:
        print(f"true")
        return True
    elif expect != array:
        print(f"false")
        return False
    
print(consec_int(array1))
print("array 2")
print(consec_int(array2))


# my_range = range(1,6)
# print(my_range) # range(1, 6)

# my_range_list = list(range(1,6))
# print(my_range_list) # [1, 2, 3, 4, 5]