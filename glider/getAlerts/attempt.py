import json

# def getAlerts(n, alert_data):
def getAlerts(n):
    """Get n alerts from some data source"""

    #json loads n (assuming json file)
    try:
        dictionary_log = json.loads(n)

        critical_counter = 0
        critital_instance = []

        fail_counter = 0
        fail_instance = []

        warning_counter = 0
        warning_instance = []
    except json.JSONDecodeError as e:
        return {
            'error': 'Invalid JSON Format'
        }
    
    try:
        for i, alert in enumerate(dictionary_log):
            # print(f"{i}, {alert}")
            if 'status' in alert:
                status = alert['status']
                if status == 'Critical':
                    critical_counter += 1
                    critital_instance.append(alert['instance_id'])
                elif status == 'Fail':
                    fail_counter += 1
                    fail_instance.append(alert['instance_id'])
                elif status == 'Warning':
                    warning_counter += 1
                    warning_instance.append(alert['instance_id'])
                else:
                    return False
        return {
            'Critical Count': critical_counter,
            'Critical Instance ID': critital_instance,
            'Fail Count': fail_counter,
            'Fail Instance ID': fail_instance,
            'Warning Count': warning_counter,
            'Warning Instance ID': warning_instance
        }
    except Exception as e:
        return f'error: {e}'
    # for loop enumerate of json file
    # check if word status exists
    # check if critical exists
    # increment counter
    # append whole log of critial systems only
    # return 




# Test data
sample_data = '''[
    {"status": "Critical", "instance_id": "i-1234", "message": "High CPU usage", "timestamp": "2025-01-15T10:30:00Z"},
    {"status": "Warning", "instance_id": "i-5678", "message": "Memory elevated", "timestamp": "2025-01-15T10:31:00Z"},
    {"status": "Critical", "instance_id": "i-9012", "message": "Service down", "timestamp": "2025-01-15T10:32:00Z"},
    {"status": "Fail", "instance_id": "i-3456", "message": "Database error", "timestamp": "2025-01-15T10:33:00Z"}
]'''

# result = getAlerts(10, sample_data)
result = getAlerts(sample_data)
print(f'result\n {result}')
# print(f"\nResults: {result['critical_count']}")