def optimize_cost_allocation(resource_costs, budget_limit):
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
        Result: 2 (remove resources costing 200 and 50 to get 200 total)
    
    Real-world: Helps with Azure cost optimization and budget management
    """
    # TODO: Implement this function
    
    # get a sum of resource costs
    total_sum = sum(resource_costs)
        # if condition: if resource costs < budget_limit return 0
    if total_sum < budget_limit :
        return 0

    # try block
    try:
    # sort resource_costs in reverese to high to low (since we want mionimum resources removed)
        sort_resource_costs = sorted(resource_costs, reverse=True)

    # initalize resource_cost = budget_limit
        current_total = total_sum
    # which resource list. init resource_cost = []
        resource_cost = []
        resource_counter = 0
    # for loop: for cost in set_resource_costs
        for cost in sort_resource_costs:
    # if condition: if resource_counter <= budget_limit
            if current_total >= budget_limit:
    # TRUE: resource_counter =- costs
                current_total =- cost
    # TRUE: resource_cost.append(cost)
                resource_cost.append(cost)
                resource_counter += 1
    # else: break
            else:
                break
    # return f"Result: resource_counter {resource_cost}
        return f"Result: {resource_counter}, suggest remove {resource_cost}"
    except Exception as e:
        print(f"Error: {e}")
        return False


resource_costs = [100, 50, 200, 75, 25]  # Total: 450
budget_limit = 300
print(optimize_cost_allocation(resource_costs, budget_limit))