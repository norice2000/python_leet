def find_missing_security_groups(required_ports, existing_rules):
    """
    CHALLENGE 2: Find Missing Security Group Rules
    
    You need to ensure specific ports (1-1000) are covered by security group rules.
    Given existing rules, find which ports are missing coverage.
    
    Args:
        required_ports (list): List of port numbers that must be accessible
        existing_rules (list): List of port ranges as tuples [(start, end), ...]
    
    Returns:
        list: Port numbers that are not covered by existing rules
    
    Example:
        required_ports = [22, 80, 443, 8080, 9000]
        existing_rules = [(20, 25), (443, 443), (8000, 9000)]
        Result: [80] (port 80 is not covered)
    
    Real-world: Ensures all required services have proper firewall access
    """
    # initliaze not_convered list
    not_covered = []
    # iterate required ports
    for port in required_ports:
        is_convered = False
    # iterate tuple start, end for existing_rules
        for start_port, end_port in existing_rules:
    # check start < req_port < end
            if start_port < port < end_port:
    # is_convered = True
                is_convered = True
    # break 
                break
    # if is_covered = False
        if not is_convered:
            not_covered.append(port)
    return not_covered
    # not_covered.append(port)

required_ports = [22, 80, 443, 8080, 9000]
existing_rules = [(20, 25), (443, 443), (8000, 9000)]
print(find_missing_security_groups(required_ports, existing_rules))