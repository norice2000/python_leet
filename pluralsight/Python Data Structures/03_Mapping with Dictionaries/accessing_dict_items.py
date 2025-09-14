settings_dict = {
    "resolution": {
        "preferences":{
            "size_1" : "1920x1080",
            "size_2" : "1080x920"
        }
    },
    "fullscreen": True,
    "volume": 75
}

print(f"Volume: {settings_dict['volume']}")

print(f"Going down the chain of resolution -> preferences -> size_2: {settings_dict['resolution']['preferences']['size_2']}")

# KeyError for looking for something that does not exist
try:
    print(f"none existing in settings: {settings_dict['tvshow']}")
except KeyError as e:
    print(f"Error: {e}")


# Checking if the Key exists
# Check if the key is NOT present
if "brightness" not in settings_dict:
    print("Brightness not found")
else:
    print(f"Brightness found: {settings_dict['brightness']}")

# Check if the key is present
if "volume" in settings_dict:
    print(f"Volume found: {settings_dict['volume']}")
else:
    print("Not found")

# Can also access the key with .get method which also allows you to assign a default value if not set
language = settings_dict.get("Language", "No Language found")
print(f"Select Language: {language}") # outputs: Select Language: No Language found

print(f"Theme: {settings_dict.get("non-existent")}") # returns None if you use this method, Theme: None

## Applying Default Values with `setdefault()`
user = {
    "username": "data_builder"
}

print(f"Prior to setdefault: {user}")
user_role = user.setdefault("dog_1", "champ")
print(f"New user with setdefault: {user['dog_1']}")
print(f"after setdefault: {user}")
# output:
# Prior to setdefault: {'username': 'data_builder'}
# New user with setdefault: champ
# after setdefault: {'username': 'data_builder', 'dog_1': 'champ'}