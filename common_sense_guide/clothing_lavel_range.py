clothing = ["Purple Shirt", "Green Shirt"]

def mark_inventory(clothing_item):
    clothing_options = []

    for item in clothing_item:
        for size in range(1, 6):
            clothing_options.append(item + " Size: " + str(size))
    return clothing_options

result = mark_inventory(clothing)
print(result)



