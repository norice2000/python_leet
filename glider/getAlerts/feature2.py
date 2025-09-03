import json

# def getAlerts(n, alert_data):
def getAlerts(n):
    """Get n alerts from some data source"""
    critical_count = 0
    fail_count = 0
    error_count = 0

    # What if json data is malformed?
    try:
        alert_logs = json.loads(n)
    except json.JSONDecodeError as e:
        print(f"Error: {e}")
        return {
            'error': 'Invalid JSON format',
            'critical_count': 0,
            'fail_count': 0,
            'error_count': 0
        }
    except Exception as e:
        return f"Error: {e}"

    # for i, alert in enumerate(alert_logs[:n]):
    for i, alert in enumerate(alert_logs): # must include i for it to iterate through each json row
        try:
            if 'status' in alert:
                status = alert['status']
                
                if status == 'Critical':
                    critical_count += 1
                elif status == 'Fail':
                    fail_count += 1
                else:
                    error_count += 1
        except Exception as e:
            print("Error: {e}")

    return {
        'critical_count': critical_count,
        'fail_count': fail_count,
        'error_count': error_count
    }

# Test data
sample_data = '''[
    {"status": "Critical", "instance_id": "i-1234", "message": "High CPU usage", "timestamp": "2025-01-15T10:30:00Z"},
    {"status": "Warning", "instance_id": "i-5678", "message": "Memory elevated", "timestamp": "2025-01-15T10:31:00Z"},
    {"status": "Critical", "instance_id": "i-9012", "message": "Service down", "timestamp": "2025-01-15T10:32:00Z"},
    {"status": "Fail", "instance_id": "i-3456", "message": "Database error", "timestamp": "2025-01-15T10:33:00Z"}
]'''

# result = getAlerts(10, sample_data)
result = getAlerts(sample_data)
print(f"\nResults: {result['critical_count']}")