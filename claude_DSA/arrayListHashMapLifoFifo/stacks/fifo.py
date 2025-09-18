# # Python lists can work as stacks!
# stack = []

# # Push (add to top)
# stack.append("first plate")
# stack.append("second plate") 
# stack.append("third plate")
# print(stack)  # ['first plate', 'second plate', 'third plate']

# # Pop (remove from top)
# top_plate = stack.pop()
# print(top_plate)  # 'third plate'
# print(stack)      # ['first plate', 'second plate']

def is_balanced(s):
    stack = []
    
    for char in s:
        if char == '(':
            stack.append(char)  # Push opening bracket
        elif char == ')':
            if not stack:  # No opening bracket to match # this is falsy which if the stack has something in it it will execute below
                return False
            stack.pop()  # Remove the matching opening bracket
    
    return len(stack) == 0  # True if all brackets were matched

# Test
# print(is_balanced("(())"))  # True
print(is_balanced("(()"))   # False