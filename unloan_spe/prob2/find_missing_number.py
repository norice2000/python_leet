from typing import List, Union, Any
from dataclasses import dataclass
import json

def find_missing_number(numbers: List[int], n: int) -> int:
    """
    CHALLENGE 4: Find Missing Number in Server IDs
    
    Given an array of n-1 integers in the range 1 to n, find the missing number.
    You have a sequence that should contain all numbers from 1 to n, but one is missing.
    
    Args:
        numbers: List of n-1 integers in range 1 to n
        n: The upper bound of the expected range
    
    Returns:
        The missing integer from the sequence
    
    Example:
        numbers = [1, 2, 4, 5, 6], n = 6
        Result: 3 (missing number from 1 to 6)
        
        numbers = [2, 3, 4, 5], n = 5  
        Result: 1 (missing number from 1 to 5)
        
        numbers = [1, 2, 3, 4], n = 5
        Result: 5 (missing number from 1 to 5)
    
    Real-world: Finding missing server IDs in a cluster, 
    detecting dropped packets in network monitoring, 
    identifying missing resource instances in cloud infrastructure
    """
    complete_set = set(range(1, n + 1))
    given_set = set(numbers)
    missing = complete_set - given_set
    return str(missing)


numbers1 = [1, 2, 4, 6]
n1 = 6
print(f"Test 1: {numbers1}, n={n1}")
print(f"Result: {find_missing_number(numbers1, n1)}")
print(f"Expected: 3")
print()

def find_missing_norange(numbers_only):

    min_num = min(numbers_only)
    max_num = max(numbers_only)
    complete_range = set(range(min_num, max_num + 1))
    given_set = set(numbers_only)
    
    return sorted(list(complete_range - given_set))

print(f"return no range: {find_missing_norange([1, 2, 3, 5, 7])}")