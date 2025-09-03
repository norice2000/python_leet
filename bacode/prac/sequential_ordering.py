class BarcodeConfigurationParser:
    def __init__(self):
        self.error_message = ["Invalid configuration"]

    def _validate_sequence_(self, parsed_config):
        print(f"parsed{parsed_config}")
        try:
            
            # Extract ordinals from tuples
            # ordinals = []
            # for config_tuple in parsed_config:
            #     ordinal_number = config_tuple[0] # we do this since we want first element '1' from the [(1, 'LAJ5KBX9H8')]
            #     ordinals.append(ordinal_number)
            # print(f"Extracted ordinals number: {str(ordinals)}")

            ordinals = [config_tuple[0] for config_tuple in parsed_config]
            print(f"Extracted ordinals number: {str(ordinals)}")
            # Sort the ordinals
            sorted_ordinals = sorted(ordinals)
            print(f"sorted_ordinals: {sorted_ordinals}")

            # Step 3: Created expected sequence [1, 2 ,3 ...N]
            num_configs = len(parsed_config) # counts how many char in a parsed config
            iterate_sequence = list(range(1, num_configs + 1))
            print(f"iterate_sequence: {iterate_sequence}, num_configs: {num_configs}")

            # Step 4 compare
            if sorted_ordinals == iterate_sequence:
                return True
            else:
                return self.error_message
                
                
        except Exception as e:
            print(f"Error: {e}")
            return self.error_message




parser = BarcodeConfigurationParser()
test_configs_1 = [(1, 'LAJ5KBX9H8'), (3, 'UKURNK403F'), (2, 'MO6K1Z9WFA'), (4, 'OWRXZFMS2C')]
result_1 = parser._validate_sequence_(test_configs_1)

# Test Case 1: Valid sequence
print("\n🟢 Test 1: Valid sequence (1,2,3,4)")
test_configs_1 = [(1, 'LAJ5KBX9H8'), (3, 'UKURNK403F'), (2, 'MO6K1Z9WFA'), (4, 'OWRXZFMS2C')]
result_1 = parser._validate_sequence_(test_configs_1)
print(f"   Final result: {result_1} (Expected: True)")

# Test Case 2: Invalid - missing ordinal 2
print("\n🔴 Test 2: Missing ordinal 2")
test_configs_2 = [(1, 'LAJ5KBX9H8'), (3, 'UKURNK403F'), (4, 'OWRXZFMS2C')]
result_2 = parser._validate_sequence_(test_configs_2)
print(f"Final result: {result_2}")

# Test Case 3: Invalid - doesn't start from 1
print("\n🔴 Test 3: Doesn't start from 1")
test_configs_3 = [(2, 'LAJ5KBX9H8'), (3, 'UKURNK403F'), (4, 'OWRXZFMS2C')]
result_3 = parser._validate_sequence_(test_configs_3)
print(f"Final result: {result_3}")

# Test Case 4: Single config (should be ordinal 1)
print("\n🟢 Test 4: Single valid config")
test_configs_4 = [(1, 'LAJ5KBX9H8')]
result_4 = parser._validate_sequence_(test_configs_4)
print(f"Final result: {result_4}")

# Test Case 5: Single config with wrong ordinal
print("\n🔴 Test 5: Single config wrong ordinal")
test_configs_5 = [(5, 'LAJ5KBX9H8')]
result_5 = parser._validate_sequence_(test_configs_5)
print(f"Final result: {result_5}")