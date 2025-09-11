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
    # TODO: Implement this function
    # try block
    # try:
    # # apply set to user_perm & required perm
    #     set_user_permission = set(user_permissions)
    #     set_required_permission = set(required_permissions)
    # # instantiate result = [] list
    #     result = []
    # # iterate through user_permission as user_perm
    #     for user_perm in set_user_permission:
    # # if condition: if user_perm not in required perms
    #         if user_perm not in set_required_permission:
    # # TRUE: append result result.append(user_perm)
    #             result.append(user_perm)
    #     return result
    # except Exception as e:
    #     print(f"Error: {e}")
    #     return False
    # # end if condition, return result
    # # exception for error

    # List Comprehension
    try:
        set_user_permission = set(user_permissions)
        set_required_permission = set(required_permissions)

        result = [user_perm for user_perm in set_user_permission if user_perm not in set_required_permission]
        return result
    except Exception as e:
        print(f"Error: {e}")
        return False

user_perms = ["read", "write", "delete", "admin", "audit"]
required_perms = ["read", "write"]
print(find_excessive_permissions(user_perms, required_perms))