def find_longest_compliant_period(security_scan_results):
    """
    CHALLENGE 4: Find Longest Security Compliance Period
    
    Given a list of daily security scan results (True = compliant, False = violation),
    find the length of the longest consecutive period of compliance.
    
    Args:
        security_scan_results (list): List of boolean values for each day
    
    Returns:
        int: Length of longest consecutive compliant period
    
    Example:
        scan_results = [True, True, False, True, True, True, False, True]
        Result: 3 (the longest sequence of True values)
    
    Real-world: Tracks security posture and compliance metrics over time
    """
    # TODO: Implement this function
    # pass
    max_length = 0
    current_length = 0

    for result in security_scan_results:
        if result == True:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
    return f"Result: {max_length}"

scan_results = [True, True, False, True, True, True, False, True]
print(find_longest_compliant_period(scan_results))