# Problem: You are given a string s. A duplicate removal consists of choosing two adjacent and equal characters 
# and removing them. We repeatedly remove duplicates until no more can be removed.
# Input: s = "abbaca"
# Output: "ca"
# Explanation: 
# - Remove "bb" → "aaca"  
# - Remove "aa" → "ca"

# Input: s = "azxxzy"  
# Output: "ay"
# Explanation:
# - Remove "xx" → "azzy"
# - Remove "zz" → "ay"

# Input: s = "aabbcc"
# Output: ""
# Explanation: Remove all pairs

#LIFO
def removeDuplicates(s):
    # Your solution here - think about when to push vs pop!
    # init stack
    # for char in s:
    # if stack and stack[-1] == char
    # stackpop
    # else
    # stack.append
    # return ",".join(sttack)

    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

# Test cases
print(removeDuplicates("abbaca"))   # Should return "ca"  
print(removeDuplicates("azxxzy"))   # Should return "ay"
print(removeDuplicates("aabbcc"))   # Should return ""
