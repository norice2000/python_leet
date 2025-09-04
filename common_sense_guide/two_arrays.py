first_array = [3, 1, 4, 2]
second_array = [4, 5, 3, 6]

def intersection(first_array: list, second_array: list) -> None:
    result = []
    for i in first_array:
        for j in second_array:
            if i == j:
                result.append(i)
    return result

print(intersection(first_array, second_array))