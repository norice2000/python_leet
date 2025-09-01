# stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# def displayInventory(inventory: dict):
#     print("Inventory:")
#     item_total = 0
#     for k, v in inventory.items():
#         print(f" {v} {k}")
#         item_total = item_total + v
#     print("Total number of items: " + str(item_total))

# displayInventory(stuff)

# List to Dictionary Function for Fantasy Game Inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    # your code goes here
    result = inventory.copy()
    for item in addedItems:
        result[item] = result.get(item, 0) + 1 # zero would default value if it finds no matches in the list
        # print(f"debug {item} : result {result}")
    # pass
    return result


def displayInventory(inventory: dict):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f" {v} {k}")
        item_total = item_total + v
    print("Total number of items: " + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)