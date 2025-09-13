"""
Platform Engineer Coding Challenge - Access Control Optimization
================================================================

PROBLEM STATEMENT:
You are managing IAM permissions for Unloan's cloud infrastructure. Given a list of 
user permissions and security policies, solve these security optimization challenges.

This tests your ability to work with lists while solving real platform security problems.

CHALLENGE DIFFICULTY: Similar to the coin change and missing number problems
REAL-WORLD APPLICATION: IAM optimization, security compliance, least privilege
"""

def find_excessive_permissions(user_permissions: list, required_permissions: list) -> list:
    """
    CHALLENGE 1: Find Excessive Permissions
    
    Given a user's current permissions and the minimum required permissions
    for their role, find which permissions can be removed (principle of least privilege).
    
    Args:
        user_permissions (list): List of permission strings the user currently has
        required_permissions (list): List of permission strings actually needed
    
    Returns:
        list: Permissions that should be removed (excessive permissions)
    
    Example:
        user_perms = ["read", "write", "delete", "admin", "audit"]
        required_perms = ["read", "write"]
        Result: ["delete", "admin", "audit"]
    
    Real-world: This helps implement least privilege in Entra ID/Auth0
    """
    # set user_perm
    # set required perms
    # for iterate in user_perm
    # if user_pem not in in user_pem
    #  append.result
    
    try:
        set_user_perm = set(user_permissions)
        set_required_perm = set(required_permissions)

        # result = copy.deepcopy(user_permissions)
        # result = []

        # for req in set_required_perm:
        #     if req in set_user_perm:
        #         result.remove(req)
        # return f"Result: {result}"
    
        # for user_perm in set_user_perm:
        #     if user_perm not in set_required_perm:
        #         result.append(user_perm)
        # return f"Result: {result}"
        # List comprehension
        result = [user_perm for user_perm in set_user_perm if user_perm not in set_required_perm]
        return f"Result: {result}"

    except Exception as e:
        print("Error: {e}")
        return e


user_perms = ["read", "write", "delete", "admin", "audit"]
required_perms = ["read", "write"]

print(find_excessive_permissions(user_perms, required_perms))
    
