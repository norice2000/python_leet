def find_missing_security_groups(required_ports: list, existing_rules: list) -> str:
    """
    CHALLENGE 2: Find Missing Security Group Rules
    
    You need to ensure specific ports (1-1000) are covered by security group rules.
    Given existing rules, find which ports are missing coverage.
    
    Args:
        required_ports (list): List of port numbers that must be accessible
        existing_rules (list): List of port ranges as tuples [(start, end), ...] #have not covered tuples YET!
    
    Returns:
        list: Port numbers that are not covered by existing rules
    
    Example:
        required_ports = [22, 80, 443, 8080, 9000]
        existing_rules = [(20, 25), (443, 443), (8000, 9000)]
        Result: [80] (port 80 is not covered)
    
    Real-world: Ensures all required services have proper firewall access
    """
    # TODO: Implement this function
    # try block
    try:
    # set required_ports to ensure no duplicates
        set_required_ports = set(required_ports)

    # set existing_rules to ensure no duplicates
        set_existing_rules = list(set(existing_rules))
    # instantiate result list
        result = []
    # iterate through existing_rules as matrix
        for exist_rule in set_existing_rules:
            for required_port in set_required_ports:
                if required_port not in exist_rule:
                    result.append(required_port)
                # print(f"{exist_rule}, {required_port}")

        return f"Result: {result} (port {str(result)}  is not covered"
    # for port_1 in existining rules 
    # for port2 in port_1
    # if condition: if port_2 not in required_ports
    except Exception as e:
        print(f"Error: {e}")
        return False


required_ports = [22, 80, 443, 8080, 9000]
existing_rules = [(20, 25), (443, 443), (8000, 9000)]
print(find_missing_security_groups(required_ports, existing_rules))