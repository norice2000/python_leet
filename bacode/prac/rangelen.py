
supply_list = ['pen', 'ruler', 'paper']
for i in range(len(supply_list)):

    print(f"Index: {i}, has {supply_list[i]}")

print("enumerate method")
for index, value in enumerate(supply_list):
    print(f"enumerate\n index: {index}, value: {value}")