# Configurations cannot skip a number in the ordering. If there are three configuration strings, there must be a 1, 2, and 3 index
# Input ordinals from parsing: [1, 3, 2, 4] (out of order)
ordinals = [1, 3, 2, 4]

# use sort
ordinal_sorted = sorted(ordinals)
print(f"ordinal_sorted: {sorted(ordinal_sorted)}") #not be confuse with sort, use sorted
# check each position
for i in range(len(ordinal_sorted)):
    # print(i)
    expected = i + 1
    actual = ordinal_sorted[i]

    print(f"Position: {i}, Expected: {expected}, Actual: {actual}")
    
# ordinal_sorted: [1, 2, 3, 4]
# Position: 0, Expected: 1, Actual: 1
# Position: 1, Expected: 2, Actual: 2
# Position: 2, Expected: 3, Actual: 3
# Position: 3, Expected: 4, Actual: 4