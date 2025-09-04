from collections import defaultdict


log_entries = [
    {"service": "api-gateway", "level": "ERROR", "message": "Connection timeout"},
    {"service": "api-gateway", "level": "ERROR", "message": "Database connection failed"},
    {"service": "user-service", "level": "WARN", "message": "High memory usage"},
    {"service": "payment-service", "level": "ERROR", "message": "Payment gateway timeout"},
    {"service": "api-gateway", "level": "INFO", "message": "Request processed"},
    {"service": "api-gateway", "level": "ERROR", "message": "Authentication failed"},
]

# print(f"without defaultdict: \n {log_entries}")

def analyse_log(logs):
    service_level = defaultdict(list)

    for log in logs:
        service = log['service']
        level = log['level']

        service_level[service].append(level)
    return dict(service_level)

check = analyse_log(log_entries)
print(check)