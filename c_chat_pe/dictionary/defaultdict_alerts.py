from collections import defaultdict
import json

# def count_errors_by_service(logs):
# def count_by_service(logs):
#     """Count how many errors each service has"""
#     error_counts = {}
#     warn_counts = {}
    
#     for log in logs:
#         if log["level"] == "ERROR":
#             service = log["service"]
            
#             # If service not in dict yet, start with 0
#             if service not in error_counts:
#                 error_counts[service] = 0
            
#             # Add 1 to the count
#             error_counts[service] += 1
#         elif log["level"] == "WARN":
#             service = log["service"]
#             if service not in warn_counts:
#                 warn_counts += 1

#     return error_counts warn_counts

def count_by_service(logs, target_level):
    service_level = defaultdict(list)

    for log in logs:
        service = log['service']
        level = log['level']

        # add if it matches the target
        if level == target_level:
            service_level[service].append(level)

def analyze_log_levels(logs):
    """See what types of logs each service produces"""
    service_levels = defaultdict(list)  # defaultdict makes this easier!
    
    for log in logs:
        service = log["service"]
        level = log["level"]
        
        # defaultdict automatically creates [] if service doesn't exist
        service_levels[service].append(level)
    
    # Convert defaultdict back to regular dict
    return dict(service_levels)

def find_connection_problems(logs):
    """Find logs mentioning connection issues"""
    connection_issues = []
    
    for log in logs:
        message = log["message"].lower()  # Convert to lowercase for searching
        
        # Look for connection-related keywords
        if "connection" in message or "timeout" in message:
            connection_issues.append({
                "service": log["service"],
                "message": log["message"]
            })
    
    return connection_issues

log_entries = [
    {"service": "api-gateway", "level": "ERROR", "message": "Connection timeout"},
    {"service": "api-gateway", "level": "ERROR", "message": "Database connection failed"},
    {"service": "user-service", "level": "WARN", "message": "High memory usage"},
    {"service": "payment-service", "level": "ERROR", "message": "Payment gateway timeout"},
    {"service": "api-gateway", "level": "INFO", "message": "Request processed"},
    {"service": "api-gateway", "level": "ERROR", "message": "Authentication failed"},
]

# Run our analysis
print("🚨 Error Counts by Service:")
# error_counts = count_errors_by_service(log_entries)
error_counts = count_by_service(log_entries, 'ERROR')
print(json.dumps(error_counts, indent=2))

# print("\n📊 Log Levels by Service:")
# log_levels = analyze_log_levels(log_entries)
# print(json.dumps(log_levels, indent=2))

# print("\n🔌 Connection Issues Found:")
# connection_problems = find_connection_problems(log_entries)
# print(json.dumps(connection_problems, indent=2))