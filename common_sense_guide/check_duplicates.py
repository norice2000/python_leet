array = [1,2,2,3]

def check_duplicates(array: list):
    return len(array) != len(set(array))

print(check_duplicates(array))