a = [1,2,3,4,5,6,6,6]
b = [4,4,5,6,7,8,9]

set_a = set(a)
print(set_a)


def merge_arrays(arrayA, arrayB):
    merge = arrayA + arrayB
    print(f"Merged: {merge}")
    set_merge = set(merge)
    print(f"Set merged: {set_merge}")
    sort_merge = sorted(set_merge)
    print(f"Sorted merge: {sort_merge}")
    return

merge_arrays(a, b)