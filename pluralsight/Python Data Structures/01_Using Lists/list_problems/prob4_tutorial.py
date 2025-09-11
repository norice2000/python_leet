def find_longest_compliant_period_solution(security_scan_results):
    """
    SOLUTION 4: Find Longest Security Compliance Period
    
    Time Complexity: O(n) - single pass through the list
    Space Complexity: O(1) - only using a few variables
    
    Teaching Notes:
    - Classic "longest consecutive subsequence" pattern
    - Use two variables: current_length and max_length
    - Reset current_length when compliance breaks
    """
    if not security_scan_results:
        return 0
    
    max_length = 0
    current_length = 0
    
    for is_compliant in security_scan_results:
        if is_compliant:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0  # Reset on violation
    
    return max_length