
def find_permission_conflicts(user_roles: Dict[str, List[str]], 
                            role_permissions: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """
    CHALLENGE 1: Find Permission Conflicts
    
    Given user role assignments and role permission definitions, find users who have
    conflicting permissions (e.g., both "read-only" and "write" permissions).
    
    Args:
        user_roles: {"user_email": ["role1", "role2", ...]}
        role_permissions: {"role_name": ["permission1", "permission2", ...]}
    
    Returns:
        Dict mapping user emails to their conflicting permissions
    
    Example:
        user_roles = {
            "alice@bluey.com": ["developer", "read-only"],
            "bob@bluey.com": ["admin", "auditor"]
        }
        role_permissions = {
            "developer": ["code-write", "deploy-staging"],
            "read-only": ["code-read"],  # Conflicts with code-write!
            "admin": ["user-manage", "system-write"],
            "auditor": ["audit-read", "system-read"]
        }
        Result: {"alice@bluey.com": ["code-write", "code-read"]} (write vs read-only conflict)
    
    Real-world: Prevents security violations in Entra ID/Auth0 role assignments
    """
    # TODO: Implement this function
    # iterate through each key
    # iterate through each value
    # 

user_roles = {
    "alice@bluey.com": ["developer", "read-only"],
    "bob@bluey.com": ["admin", "auditor"]
}
role_permissions = {
    "developer": ["code-write", "deploy-staging"],
    "read-only": ["code-read"],  # Conflicts with code-write!
    "admin": ["user-manage", "system-write"],
    "auditor": ["audit-read", "system-read"]
}
print(find_permission_conflicts(user_roles, role_permissions))