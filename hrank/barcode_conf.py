#Expected output: ["LAJ5KBX9H8", "MO6K1Z9WFA", "UKURNK403F", "OWRXZFMS2C"]
# Input format:
# "0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C"
#     ↑   ↑           ↑   ↑
#     │   │           │   └─ Configuration value (10 chars)
#     │   └─ Config    └─ Ordinal index (4 digits)
#     └─ Ordinal (4 digits)



def test_barcode_configuration():
    """Test all cases - valid and invalid"""
    
    test_cases = [
        # Valid cases
        {
            "name": "Valid - Simple case",
            "input": "0001LAJ5KBX9H8|0002MO6K1Z9WFA",
            "expected": ["LAJ5KBX9H8", "MO6K1Z9WFA"]
        },
        {
            "name": "Valid - Out of order input",
            "input": "0001LAJ5KBX9H8|0003UKURNK403F|0002MO6K1Z9WFA|0004OWRXZFMS2C",
            "expected": ["LAJ5KBX9H8", "MO6K1Z9WFA", "UKURNK403F", "OWRXZFMS2C"]
        },
        
        # Invalid cases
        {
            "name": "Invalid - Wrong total length",
            "input": "0001SHORT|0002MO6K1Z9WFA",
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Non-digit ordinal", 
            "input": "000ALAJ5KBX9H8|0002MO6K1Z9WFA",
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Config too long",
            "input": "0001TOOLONG1234|0002MO6K1Z9WFA",  # TOOLONG1234 = 11 chars
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Config too short", 
            "input": "0001SHORT12|0002MO6K1Z9WFA",      # SHORT12 = 7 chars
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Config not alphanumeric",
            "input": "0001LAJ5KB-9H8|0002MO6K1Z9WFA",
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Ordinal 0000",
            "input": "0000LAJ5KBX9H8|0001MO6K1Z9WFA", 
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Duplicate ordinals",
            "input": "0001LAJ5KBX9H8|0001DIFFERENTX",
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Duplicate configs",
            "input": "0001LAJ5KBX9H8|0002LAJ5KBX9H8",
            "expected": ["Invalid configuration"]
        },
        {
            "name": "Invalid - Skipped number",
            "input": "0001LAJ5KBX9H8|0003UKURNK403F",  # Missing 0002
            "expected": ["Invalid configuration"]
        }
    ]
    
    print("🧪 Testing Barcode Configuration Parser\n")
    
    for i, test in enumerate(test_cases):
        result = ordered_configuration(test["input"])
        passed = result == test["expected"]
        status = "✅ PASS" if passed else "❌ FAIL"
        
        print(f"Test {i+1}: {test['name']}")
        print(f"Input: {test['input'][:50]}{'...' if len(test['input']) > 50 else ''}")
        print(f"Expected: {test['expected']}")
        print(f"Got:      {result}")
        print(f"Status: {status}\n")

# Run the tests
if __name__ == "__main__":
    # Your solution here
    def ordered_configuration(configuration: str):
        # print(f"debug: input: {configuration}")
        try:
            parts = configuration.split("|") #All configurations must be separated by a "|" character
            configs = []
            
            # STEP 1: Process each part individually -
            for index, part in enumerate(parts):

                # Each part should be exactly 14 chars (4 ordinal + 10 config)
                if len(part) != 14:
                    return ['Invalid configuration']
                
                # seperate ordinal and config digit
                ordinal_str = part[:4] # first 4
                config_str = part[4:] # last 10

                # Ordinal index should be 4 digit numeric
                if not ordinal_str.isdigit():
                    return ['Invalid configuration']
                # Configuration value length is exactly 10 characters"
                if len(config_str) != 10:
                    return ['Invalid configuration']
                #Configuration values are alphanumeric and may contain no other characters
                if not config_str.isalnum():
                    return ['Invalid configuration']
                
                #convert ordinal to int
                ordinal_int = int(ordinal_str)
                # first ordinal set of 4 cannot be 0
                if ordinal_int == 0:
                    return ['Invalid configuration']
                
                configs.append((ordinal_int, config_str)) # config[0] is ordinal, config[1] is configure

            #Configurations cannot skip a number in the ordering. If there are three configuration strings, there must be a 1, 2, and 3 index
            ordinals = [config[0] for config in configs] #assigning first item from typle since thay are ordinal
            config_values = [config[1] for config in configs] #assigning second item from typle since thyre configs

            # Check for duplicate ordinals
            if len(ordinals) != len(set(ordinals)):
                return ['Invalid configuration']
            # Check for duplicate configs
            if len(config_values) != len(set(config_values)):
                return ['Invalid configuration']
            

# for config in configs:
#     ordinal_num = config[0]    # Get first item from tuple
#     config_str = config[1]     # Get second item from tuple
#     ordinals.append(ordinal_num)
#     config_values.append(config_str)

# # But list comprehension is much shorter!
# ordinals = [config[0] for config in configs]
# config_values = [config[1] for config in configs]

            # Configurations cannot skip a number in the ordering. If there are three configuration strings, 
            # there must be a 1, 2, and 3 index
            # start sorting 
            ordinals_sorted = sorted(ordinals)
            for i in range(len(ordinals_sorted)):
                expected = i + 1
                actual = ordinals_sorted[i]
                if actual != expected:
                    return ['Invalid configuration']
                
            configs.sort()
            result = [config[1] for config in configs]
            return result
            


        except Exception as e:
            return ['Invalid configuration']
    
    test_barcode_configuration()