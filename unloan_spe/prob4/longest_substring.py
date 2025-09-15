def length_longest_substring_optimal(s):
    """
    Optimal solution using sliding window technique
    Time: O(n), Space: O(min(m,n)) where m is charset size
    """
    char_set = set()  # Track characters in current window
    left = 0          # Left pointer of sliding window
    max_length = 0    # Track maximum length found
    
    print(f"\n🔍 Processing string: '{s}'")
    print("=" * 50)
    
    for right in range(len(s)):
        current_char = s[right]
        print(f"\nStep {right + 1}: Processing character '{current_char}' at index {right}")
        
        # Shrink window from left until no duplicate
        while current_char in char_set:
            removing_char = s[left]
            char_set.remove(removing_char)
            print(f"  ❌ Found duplicate '{current_char}'! Removing '{removing_char}' from window")
            print(f"  📍 Moving left pointer from {left} to {left + 1}")
            left += 1
            print(f"  🪟 Current window: {char_set}")
        
        # Add current character to window
        char_set.add(current_char)
        current_length = right - left + 1
        print(f"  ✅ Added '{current_char}' to window")
        print(f"  🪟 Current window: {char_set}")
        print(f"  📏 Current substring: '{s[left:right+1]}' (length: {current_length})")
        
        # Update maximum length
        if current_length > max_length:
            max_length = current_length
            print(f"  🎉 New maximum length: {max_length}")
        else:
            print(f"  📊 Max length remains: {max_length}")
    
    print(f"\n🏆 Final result: {max_length}")
    return max_length

test_cases = [
    "abcabcbb",   # Expected: 3 ("abc")
    # "bbbbb",      # Expected: 1 ("b") 
    # "pwwkew",     # Expected: 3 ("wke")
    # "",           # Expected: 0
    # "abcdef",     # Expected: 6 (entire string)
    # "a",          # Expected: 1
    # "au",         # Expected: 2
    # "aab",        # Expected: 2 ("ab")
]

print(length_longest_substring_optimal(test_cases))