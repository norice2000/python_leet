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
    try:
        total_costs = sum(resource_costs)

        if total_costs <= budget_limit:
            return 0
        
        removed_counter = 0
        remove_resource = []
        current_total = total_costs
        sort_resource_costs = sorted(resource_costs,reverse=True)

        for cost in sort_resource_costs:
            if current_total > budget_limit:
                current_total -= cost
                remove_resource.append(cost)
                removed_counter += 1
            else:
                break

        return f"Result: {removed_counter} (remove resource: {str(remove_resource)})"
    except Exception as e:
        print("Error: {e}")
        return False


resource_costs = [100, 50, 200, 75, 25]  # Total: 450
budget_limit = 300

print(optimize_cost_allocation(resource_costs, budget_limit))