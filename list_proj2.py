# pizzas = ["pepperoni", "cheese", "pineapple"]

# for pizza in pizzas:
#     print(f"I like {pizza} pizza")

# print("ALl great pizzas")


# list comprehension
# new_list = [EXPRESSION for ITEM in ITERABLE]
# #           ↑          ↑   ↑    ↑
# #           │          │   │    └─ What to loop through
# #           │          │   └─ Variable name for each item  
# #           │          └─ Python keyword
# #           └─ What to calculate/transform

# like_pizza = [f"I like {pizza}" for pizza in pizzas]
# print(like_pizza)

# # Traditional way
# servers = ['web-01', 'web-02', 'db-01']
# server_urls = []
# for server in servers:
#     server_urls.append(f"https://{server}.company.com")

# # List comprehension way
# servers = ['web-01', 'web-02', 'db-01'] 
# server_urls = [f"https://{server}.company.com" for server in servers]
# print(server_urls)  
# # ['https://web-01.company.com', 'https://web-02.company.com', 'https://db-01.company.com']


# dogs = ['champ','lucky','lulu', 'as']
# list_compre = [dog.title() for dog in dogs if len(dog) >= 3]
# print(list_compre)



barcode = "0001LAJ5KBX9H8|0003UKURNK403F"

split_bar = barcode.split("|")
configs = []

for index, part in enumerate(split_bar):
    ordinal_index = part[:4]
    config_index = part[4:]

    ordinal_num = int(ordinal_index) #this removes from 0001 to 1
    configs.append(ordinal_num, config_index)
    
    ordinals = []
    config_values = []
    for config in configs:
        ordinals.append(config[0]) #append adds object end of the list
        config_values.append(config[1])
    print(ordinals)
    print(config_values)

print(ordinal_index)
print(config_index)

