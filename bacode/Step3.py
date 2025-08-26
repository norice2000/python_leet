# In OOP, we break complex problems into smaller pieces using methods (functions that belong to a class). 
# Each method should have one clear responsibility.
# Step 3: Adding Our First Method - Splitting the String

class BarcodeConfigurationParser:
    def __init__(self):
        self.error_message = ['Invalid configuration']

    def _split_configurations(self, config_string)

    def parse(self, config_string: str): # def METHOD( attributes)
        print(f"Recieved config string: {config_string}")
        return ['We will build this step by step']
    
# Testing basic class
parser = BarcodeConfigurationParser()
result = parser.parse("0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C")
print(f"Result: {result}")

## Output:
# Recieved config string: 0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C
# Result: ['We will build this step by step']

