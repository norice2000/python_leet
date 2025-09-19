# Problem: Given a string s containing just the characters '()', '[]' and '{}', determine if the input string is valid.

def isValid(s):
    result = []
    valid_pairs = {
        '(': ')', 
        '[':']',
        '{':'}'
    }

    for char in s:
        if char in valid_pairs.keys():
            result.append(char)
        elif char in valid_pairs.values():
            if not result:
                return False
            opening = result.pop()
            if valid_pairs[opening] != char:
                return False
    return len(result) == 0

# Test cases
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True  
print(isValid("(]"))        # False
print(isValid("([{}])"))    # True
print(isValid("([)]"))      # False - remember this tricky one!