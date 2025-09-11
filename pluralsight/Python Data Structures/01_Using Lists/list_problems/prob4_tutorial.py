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
## Understanding max()
# Let's trace through this:
# max_length = 5      # I had a 5-day streak before
# current_length = 3  # Current streak is only 3 days

# max_length = max(max_length, current_length)
# max_length = max(5, 3)  # Which is bigger, 5 or 3?
# max_length = 5          # Keep the old record!

    max_length = 0
    current_length = 0

    for result in security_scan_results:
        if result: # pythonic way of saying result == True # Know the alternatives: if not is_compliant: means "if False"
            current_length += 1
            max_length = max(max_length, current_length) #this will compare the int of max_length & current_length to see which one is larger to be re-assigned as max_length
        else:
            current_length = 0
    return f"Result: {max_length}"

scan_results = [True, True, False, True, True, True, False, True]
print(find_longest_compliant_period(scan_results))