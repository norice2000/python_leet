# Problem: Given a string s containing just the characters '()', '[]' and '{}', determine if the input string is valid.

def isValid(s):
    seen = []
    valid_param = {
        '(': ')', 
        '[':']',
        '{':'}'
    }

    # for char in seen
    # if char in valid_param.keys
    # append.seen[char]
    # elif char in valid_params.values()
    # opening = seen.pop()
    # if valid_param[opening] != char:
    # return False
    #return len(seen) == 0 #true

    for char in s:
        if char in valid_param.keys():
            seen.append(char)
        elif char in valid_param.values():
            if valid_param[seen.pop()] != char:
                return False
    return len(seen) == 0 # True
# Test cases
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True  
print(isValid("(]"))        # False
print(isValid("([{}])"))    # True
print(isValid("([)]"))      # False - remember this tricky one!