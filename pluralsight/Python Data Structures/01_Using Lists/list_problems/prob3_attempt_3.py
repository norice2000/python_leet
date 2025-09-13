def optimize_cost_allocation(resource_costs: list, budget_limit: int) -> str:
    """
    CHALLENGE 3: Optimize Azure Resource Allocation
    
    Given a list of Azure resources with their monthly costs, find the minimum
    number of resources to remove to stay within budget.
    
    Args:
        resource_costs (list): List of monthly costs for each resource
        budget_limit (int): Maximum allowed monthly budget
    
    Returns:
        int: Minimum number of resources to remove
    
    Example:
        resource_costs = [100, 50, 200, 75, 25]  # Total: 450
        budget_limit = 300
        Result: 1 (remove resources costing 200 and 50 to get 200 total)
    
    Real-world: Helps with Azure cost optimization and budget management
    """
    # TODO: Implement this function
    # sum of a list
    # try block
    # total_cost = budget_limit
    # for i in resource_cost
    # if total_cost <= budget:
    #   total_cost =- i
    # return total_cost

    try:
        total_cost = sum(resource_costs)
        sort_resource_cost = sorted(resource_costs, reverse=True)
        
        for cost in sort_resource_cost:
            if total_cost >= budget_limit:
                total_cost -= cost
        return total_cost

    except Exception as e:
        return e

resource_costs = [100, 50, 200, 75, 25]  # Total: 450
budget_limit = 300

print(optimize_cost_allocation(resource_costs, budget_limit))