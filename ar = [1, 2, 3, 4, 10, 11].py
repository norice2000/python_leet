a = [5,6,7]
b = [3,6,10]
a_counter = 0
b_counter = 0
result = [a_counter, b_counter]

for i in range(3):
    if a[i] > b[i]:
        a_counter += 1
    elif a[i] == b[i]:
        continue
    elif a[i] < b[i]:
        b_counter += 1
    else:
        continue
print([a_counter, b_counter])