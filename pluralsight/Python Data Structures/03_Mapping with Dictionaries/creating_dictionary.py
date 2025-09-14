# Dictionary, which has 3 elements, and the item is a key value pairs
# Dictionary keys must be immutable because they need to be hashable
settings_dict = {
    "resolution": "1920x1080",
    "fullscreen": True,
    "volume": 75
}

print(f"Settings dict: {settings_dict}")
print(f"Length of dictionary: {len(settings_dict)}")
print(f"Resolution: {settings_dict['resolution']}")


# Iniitalize Dictionary Values with `dict.fromkeys()`

permissions = ["read", "write", "delete", "export"]
default_permission = dict.fromkeys(permissions, None) #making each key output as None

print(f"default_permission: {default_permission}")
# output: default_permission: {'read': None, 'write': None, 'delete': None, 'export': None}