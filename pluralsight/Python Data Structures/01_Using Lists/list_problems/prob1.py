"""
Platform Engineer Coding Challenge - Access Control Optimization
================================================================

PROBLEM STATEMENT:
You are managing IAM permissions for Bluey's cloud infrastructure. Given a list of 
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
    # TODO: Implement this function
    ...
    try:
        set_user_permissions = set(user_permissions) # use set to ensure no duplicates
        set_required_permissions = set(required_permissions) # use set to ensure no duplicates
        # result = []

        # for user_perm in set_user_permissions: #iterate of user_permissions
        #     if user_perm not in set_required_permissions: #  iterate user_perm and check if it does NOT exists in the required_perms, 
        #         result.append(user_perm) # TRUE, append result
        # return result

        # list comprehension
        result = [user_perm for user_perm in set_user_permissions if user_perm not in set_required_permissions]
        return result


    except Exception as e:
        print(f"error: {e}")
        return False

user_perms = ["read", "write", "delete", "admin", "audit"]
required_perms = ["read", "write"]
print(str(find_excessive_permissions(user_perms, required_perms)))
