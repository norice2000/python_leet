# Problem: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward.
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Input: s = "race a car"  
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Input: s = " "
# Output: true (empty string is palindrome)

def isPalindrome(s: str):
    def clean_string(text):  # Add parameter
        result = ""
        for char in text:
            if char.isalnum():
                result += char.lower()
        return result
    
    clean = clean_string(s)
    ## Two Pointers
    left = 0
    right = len(clean) - 1  # Use clean, not s
    
    while left < right: # this makes sure that R and L cannot cross each other
        if clean[left] != clean[right]:
            return False
        left += 1
        right -= 1
    return True

# Test cases
print(isPalindrome("A man, a plan, a canal: Panama"))  # True
# print(isPalindrome("race a car"))                      # False  
# print(isPalindrome(" "))                              # True