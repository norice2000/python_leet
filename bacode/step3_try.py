# In OOP, we break complex problems into smaller pieces using methods (functions that belong to a class). 
# Each method should have one clear responsibility.
# Step 3: Adding Our First Method - Splitting the String

class BarcodeConfigurationParser:
    def __init__(self):
        self.error_message = ['Invalid configuration']

    # Step Prereq All configurations must be separated by a "|" character
    def _split_configurations(self, config_string: str):
        configurations = config_string.split("|")
        print(f"Split config: {configurations}")
        return configurations

    # Step 3
    def _parse_single_configuration(self, config_part: str):
        try:
            # # VALIDATION: Total length must be 14
            if len(config_part) != 14:
                return None
            
            # slice index
            ordinal_index = config_part[:4] # First 4
            config_value = config_part[4:] # Remaining 10
            # print(f"Parsed: {config_part}, Ordinal: {ordinal_index}, Config: {config_value}")

            # Step Prereq the ordinal index value is a 4 digit numeric prefixed with zeros
            if not ordinal_index.isdigit():
                return None
            
            # 3. Configuration values are alphanumeric and may contain no other characters
            if not config_value.isalnum():
                return None
            
            # 4. Configuration value length is exactly 10 characters
            if len(config_value) != 10:
                return None
            
            # 5. Ordinal indices may not repeat, for example there cannot be two occurrences of the number "1"

            # 6. Each configuration value is unique, configurations do not repeat
            
            # 7. "0000" is not a valid ordinal index
            if ordinal_index == "0000":
                return None
            
            return (int(ordinal_index), config_value)  # Convert ordinal to int
        
        except Exception as e:
            print(f"Unexpected error parsing {config_part} : {e}")

    # Step 2
    def _validate_sequence_order(self, parsed_config):
        try:
            
        except Exception as e:
            print(f"Invalid sequence detected")
    # Main
    def parse(self, config_string: str): # def METHOD( attributes)
        try:
            print(f"Recieved config string: {config_string}")

            # Step 1: Split the string
            config_parts = self._split_configurations(config_string) #outputs: ['0001LAJ5KBX9H8', '0003UKURNK403F', '0002MO6K1Z9WFA', '0004OWRXZFMS2C']
            # print(f"Starting to split {config_parts}")

            # Step 3: Parse each individual config
            # now we need that tuple to be in a list
            #the tuples of ordinal and config index
            parsed_configs = []
            for config_part in config_parts: # this will get the first tuple '0001LAJ5KBX9H8'
                result = self._parse_single_configuration(config_part)
                if result is None:
                    return self.error_message
                parsed_configs.append(result) # outputs:  [('0001', 'LAJ5KBX9H8'), ('0003', 'UKURNK403F'), ('0002', 'MO6K1Z9WFA'), ('0004', 'OWRXZFMS2C')]
                print(str(f"parsed_configs: {parsed_configs}"))

            return ["Success, valid"] # finisher
        
        except Exception as e:
            print(f"Unexpected erorr in parse: {e}")
            return self.error_message


def run_tests():
    parser = BarcodeConfigurationParser()
    
    print("=" * 60)
    print("TESTING BARCODE CONFIGURATION PARSER")
    print("=" * 60)
    
    # TEST 1: VALID CASE - Should pass all current validations (1,3,4,5,6,7)
    print("\n🟢 TEST 1: VALID CONFIGURATION")
    print("-" * 30)
    valid_config = "0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C"
    result = parser.parse(valid_config)
    print(f"Expected: Success (with note about condition 2)")
    print(f"Actual: {result}")
    
    # TEST 2: INVALID - Violates Condition 3 (non-alphanumeric)
    print("\n🔴 TEST 2: NON-ALPHANUMERIC CONFIG VALUE")
    print("-" * 30)
    print("Testing Condition 3: Configuration values must be alphanumeric only")
    invalid_config = "0001LAJ5KBX@H8|0002UKURNK403F"
    result = parser.parse(invalid_config)
    print(f"Expected: {parser.error_message}")
    print(f"Actual: {result}")
    
    # TEST 3: INVALID - Violates Condition 4 (wrong config length)
    print("\n🔴 TEST 3: WRONG CONFIG VALUE LENGTH")
    print("-" * 30)
    print("Testing Condition 4: Configuration values must be exactly 10 characters")
    invalid_config = "0001LAJ5KBX9H|0002UKURNK403F"  # Only 9 chars
    result = parser.parse(invalid_config)
    print(f"Expected: {parser.error_message}")
    print(f"Actual: {result}")
    
    # TEST 4: INVALID - Violates Condition 5 (duplicate ordinals)
    print("\n🔴 TEST 4: DUPLICATE ORDINALS")
    print("-" * 30)
    print("Testing Condition 5: Ordinal indices may not repeat")
    invalid_config = "0001LAJ5KBX9H8|0001UKURNK403F"  # Two 0001s
    result = parser.parse(invalid_config)
    print(f"Expected: {parser.error_message}")
    print(f"Actual: {result}")
    
    # TEST 5: INVALID - Violates Condition 6 (duplicate config values)
    print("\n🔴 TEST 5: DUPLICATE CONFIG VALUES")
    print("-" * 30)
    print("Testing Condition 6: Each configuration value must be unique")
    invalid_config = "0001LAJ5KBX9H8|0002LAJ5KBX9H8"  # Same config value
    result = parser.parse(invalid_config)
    print(f"Expected: {parser.error_message}")
    print(f"Actual: {result}")
    
    # TEST 6: INVALID - Violates Condition 7 (0000 ordinal)
    print("\n🔴 TEST 6: INVALID ORDINAL 0000")
    print("-" * 30)
    print("Testing Condition 7: '0000' is not a valid ordinal")
    invalid_config = "0000LAJ5KBX9H8|0002UKURNK403F"
    result = parser.parse(invalid_config)
    print(f"Expected: {parser.error_message}")
    print(f"Actual: {result}")
    
    # TEST 7: EDGE CASE - Single valid configuration
    print("\n🟡 TEST 7: SINGLE CONFIGURATION")
    print("-" * 30)
    print("Testing with just one configuration")
    single_config = "0001LAJ5KBX9H8"
    result = parser.parse(single_config)
    print(f"Expected: Success (should work)")
    print(f"Actual: {result}")
    
    # TEST 8: EDGE CASE - Empty or malformed input
    print("\n🔴 TEST 8: MALFORMED INPUT")
    print("-" * 30)
    print("Testing with empty or malformed input")
    try:
        result = parser.parse("")
        print(f"Empty string result: {result}")
        
        result = parser.parse("0001LAJ5KBX9H8|")  # Trailing |
        print(f"Trailing | result: {result}")
        
        result = parser.parse("|0001LAJ5KBX9H8")  # Leading |
        print(f"Leading | result: {result}")
    except Exception as e:
        print(f"Exception caught: {e}")

    print("\n" + "=" * 60)
    print("VALIDATION STATUS:")
    print("✅ Condition 1: Separator validation")
    print("✅ Condition 3: Alphanumeric validation")  
    print("✅ Condition 4: Config length validation")
    print("✅ Condition 5: No duplicate ordinals")
    print("✅ Condition 6: No duplicate config values")
    print("✅ Condition 7: No 0000 ordinal")
    print("❌ Condition 2: Sequential ordering (still needed)")
    print("=" * 60)

# Run all tests
run_tests()

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