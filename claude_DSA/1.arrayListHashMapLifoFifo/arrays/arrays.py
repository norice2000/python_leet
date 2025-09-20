# A list is our first data structure!
fruits = ["apple", "banana", "orange"]

def find_largest(numbers):
    # Start with the first number as our "current largest"
    largest = numbers[0]
    
    # Check each number in the list
    for num in numbers:
        if num > largest:
            largest = num
    
    return largest

# Test it
numbers = [3, 7, 2, 9, 1]
print(find_largest(numbers))  # Should print 9


def find_smallest(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest

numbers = [3, 7, 2, 9, 1]
print(find_smallest(numbers))  # Should print 1