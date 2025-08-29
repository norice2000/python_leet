# In OOP, we break complex problems into smaller pieces using methods (functions that belong to a class). 
# Each method should have one clear responsibility.
# Step 3: Adding Our First Method - Splitting the String

class BarcodeConfigurationParser:
    def __init__(self):
        self.error_message = ['Invalid configuration']

    # Step 1
    def _split_configurations(self, config_string: str):
        configurations = config_string.split("|")
        print(f"Split config: {configurations}")
        return configurations

    # Step 2
    def _parse_single_configuration(self, config_part: str):
        if len(config_part) != 14:
            return self.error_message
        
        # slice index
        ordinal_index = config_part[:4] # First 4
        config_value = config_part[4:] # Remaining 10

        print(f"Parsed: {config_part}, Ordinal: {ordinal_index}, Config: {config_value}")
        return (ordinal_index, config_value) # returning a tuple

    # Main
    def parse(self, config_string: str): # def METHOD( attributes)
        print(f"Recieved config string: {config_string}")

        # Step 1: Split the string
        config_parts = self._split_configurations(config_string) #outputs: ['0001LAJ5KBX9H8', '0003UKURNK403F', '0002MO6K1Z9WFA', '0004OWRXZFMS2C']
        print(f"Starting to split {config_parts}")

        # Step 2: Parse each individual config
        # now we need that tuple to be in a list
        #the tuples of ordinal and config index
        parsed_configs = []
        for config_part in config_parts: # this will get the first tuple '0001LAJ5KBX9H8'
            result = self._parse_single_configuration(config_part)
            parsed_configs.append(result) # outputs:  [('0001', 'LAJ5KBX9H8'), ('0003', 'UKURNK403F'), ('0002', 'MO6K1Z9WFA'), ('0004', 'OWRXZFMS2C')]
            print(str(f"parsed_configs: {parsed_configs}"))
            if result is None:
                return self.error_message
        

        return ['We will build this step by step']
    
# Testing basic class
parser = BarcodeConfigurationParser()
result = parser.parse("0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C")
print(f"Result: {result}")



## Output:
# Recieved config string: 0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C
# Result: ['We will build this step by step']


# The underscore is like a sign that says "Internal Use Only"

# PUBLIC methods (no underscore):
# - These are your "contract" with users
# - You promise these will work and stay stable
# - Users should feel safe calling these
# - Example: parse(), get_error_message()

# PRIVATE methods (with underscore):
# - These are implementation details
# - You might change or remove them later
# - Users shouldn't rely on these existing
# - Example: _split_configurations(), _validate_ordinal_index()
# """)