def is_balanced_multi(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}  # Map opening to closing
    
    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack:
                return False # prints if stack is empty
            if pairs[stack.pop()] != char:  # Wrong closing bracket!
                return False
    
    return len(stack) == 0

# Test cases
# print(is_balanced_multi("()"))      # True
# print(is_balanced_multi("()[]{}"))  # True  
# print(is_balanced_multi("([{}])"))  # True
print(is_balanced_multi("([)]"))    # False - wrong order!