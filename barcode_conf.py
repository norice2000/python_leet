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
            "name": "Invalid - Config not 10 chars",
            "input": "0001TOOLONG123|0002MO6K1Z9WFA",
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
            part = configuration.split("|") #All configurations must be separated by a "|" character
            # print(f"after split: {part}")
            configs = []

            for index, part in enumerate(part):
                # print(f"index: {index + 1}\n part: {part}")
                # print(f"Checking length: {len(part)}")

                # Each part should be exactly 14 chars (4 ordinal + 10 config)
                if len(part) >= 14:
                    return ['Invalid configuration']
                
                # seperate ordinal and config digit
                ordinal_str = part[:4] # first 4
                config_str = part[4:] # last 10
                print(f"ordinal: {ordinal_str}")
                print(f"config: {config_str}")

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

                print(f"config {configs}")
                #Configurations cannot skip a number in the ordering. If there are three configuration strings, there must be a 1, 2, and 3 index
                for i in configs[0]:
                    ordinals = i
                
                print(f"final: {configs.append(ordinal_int, config_str)}")
            
        except Exception as e:
            return ['Invalid configuration']
    
    test_barcode_configuration()