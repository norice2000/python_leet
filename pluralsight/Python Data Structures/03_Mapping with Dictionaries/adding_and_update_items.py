# Adding and updating items

books = {
    "book_1": "Buff baby"
}

print(f"books: {books}")
books['book_2'] = 'cookbook'
print(f"addded cookbook: {books}")
books['book_1'] = 'linuxbook'
print(f"change dict for book_1: {books}")

# Updating multiple of dictionary with `update()`
settings ={
    "volume": 22,
    "language": "english"
}

override_settings = {
    "volume": 40,               #changing existing value
    "tv_show": "demon_slayer"   # adding a new key value
}

settings.update(override_settings)
# new python version now has the MERGE operator which is | or =|
new_settings = settings | override_settings
print(f"merging method: {new_settings}")
print(settings)
# output: {'volume': 40, 'language': 'english', 'tv_show': 'demon_slayer'}