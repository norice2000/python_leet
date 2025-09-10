# CHALLENGE 1: Identity Access Policy Enforcement
# ==============================================

def demonstrate_access_policy_problem():
    """
    PROBLEM: Given user roles and resource access requirements,
    determine if access should be granted based on least-privilege principles.
    
    This tests your understanding of IAM and security controls.
    """
    print("=== CHALLENGE 1: ACCESS POLICY ENFORCEMENT ===")
    print("You need to implement least-privilege access control")
    print("Users have roles, resources have required permissions")
    print("Grant access only if user has EXACT required permissions (no more, no less ideal)")
    
    # Sample data structure
    users = {
        "alice@unloan.com": {
            "roles": ["developer", "read-prod"],
            "department": "engineering"
        },
        "bob@unloan.com": {
            "roles": ["admin", "write-prod"], 
            "department": "platform"
        }
    }
    
    role_permissions = {
        "developer": ["code-read", "deploy-staging"],
        "admin": ["user-manage", "resource-create"],
        "read-prod": ["prod-read"],
        "write-prod": ["prod-read", "prod-write"]
    }
    
    resource_requirements = {
        "production-database": ["prod-read"],
        "user-management": ["user-manage"],
        "staging-deploy": ["deploy-staging"]
    }
    
    return users, role_permissions, resource_requirements

# TO DO
# create function that accepts users if the data structure parsed in which is a ditionary with list

def main()
# Check if user exists
# Get required permissions

# calc user actual permission
# chheck if user has required permission