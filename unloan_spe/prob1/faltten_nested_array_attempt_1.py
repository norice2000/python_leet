from typing import List, Union, Any
from dataclasses import dataclass
import json

def flatten_nested_array(nested_array: List[Union[int, List]]) -> List[int]:
    """
    CHALLENGE 3: Flatten Nested Configuration Arrays
    
    Given a nested array structure containing numbers and sub-arrays,
    flatten it into a single-level array containing all numbers in order.
    
    Args:
        nested_array: List containing integers and nested lists of integers
    
    Returns:
        List of integers in flattened order
    
    Example:
        nested_config = [1, [2, [3, 4]], 5, [6, 7]]
        Result: [1, 2, 3, 4, 5, 6, 7]
        
        nested_config = [10, [20, 30], [40, [50, 60]], 70]
        Result: [10, 20, 30, 40, 50, 60, 70]
    
    Real-world: Flattening hierarchical configuration structures, 
    processing nested Terraform/YAML configurations, log aggregation
    """
    # TODO
    # initialize result
    # iterate through elements
    # if isinstance(element, list)
    # update result at the end, result.extend
    # else: update result at the start result.append
    # returnr result

    try:
        result = []

        for i in nested_array:
            if isinstance(i, list):
                result.extend(flatten_nested_array(i))
            else:
                result.append(i)
        return result
    except Exception as e:
        return e


nested_config = [10, [20, 30], [40, [50, 60]], 70]
print(flatten_nested_array(nested_config))