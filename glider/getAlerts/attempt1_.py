from datetime import datetime
from collections import Counter
from typing import List, Dict, Any

def getAlerts(n: int, alerts_db: List[Dict] = None) -> List[Dict]:
    """
    Returns the last n alerts from the system.
    In a real system, this would query a database or message queue.
    """
    if alerts_db is None:
        alerts_db = sample_alerts
    
    # Sort by timestamp descending to get most recent first
    sorted_alerts = sorted(alerts_db, 
        key=lambda x: datetime.fromisoformat(x['timestamp'].replace('Z', '+00:00')), 
        reverse=True)
    
    return sorted_alerts[:n]

def filterCriticalAlerts(alerts: List[Dict]) -> List[Dict]:
    """
    Filters and returns only alerts with 'critical' severity.
    """
    return [alert for alert in alerts if alert.get('severity') == 'critical']

def analyzeAlerts(critical_alerts: List[Dict]) -> Dict[str, Any]:
    """
    Analyzes critical alerts and returns comprehensive summary information.
    """
    if not critical_alerts:
        return {
            "total_critical": 0,
            "unresolved_critical": 0,
            "services_affected": [],
            "unacknowledged_count": 0,
            "top_service_by_alerts": None,
            "most_recent_critical": None,
            "average_metric_value": 0
        }
    
    # Basic counts
    total_critical = len(critical_alerts)
    unresolved_critical = sum(1 for alert in critical_alerts if not alert.get('resolved', True))
    
    # Services affected
    services_affected = list(set(alert['service'] for alert in critical_alerts))
    
    # Unacknowledged alerts (acknowledgements = 0)
    unacknowledged_count = sum(1 for alert in critical_alerts if alert.get('acknowledgements', 0) == 0)
    
    # Service with most alerts
    service_counts = Counter(alert['service'] for alert in critical_alerts)
    top_service_by_alerts = service_counts.most_common(1)[0][0] if service_counts else None
    
    # Most recent critical alert
    if critical_alerts:
        most_recent = max(critical_alerts, 
            key=lambda x: datetime.fromisoformat(x['timestamp'].replace('Z', '+00:00')))
        most_recent_critical = most_recent['timestamp']
    else:
        most_recent_critical = None
    
    # Average metric value
    metric_values = [alert.get('metric_value', 0) for alert in critical_alerts if alert.get('metric_value') is not None]
    average_metric_value = round(sum(metric_values) / len(metric_values), 2) if metric_values else 0
    
    return {
        "total_critical": total_critical,
        "unresolved_critical": unresolved_critical,
        "services_affected": services_affected,
        "unacknowledged_count": unacknowledged_count,
        "top_service_by_alerts": top_service_by_alerts,
        "most_recent_critical": most_recent_critical,
        "average_metric_value": average_metric_value
    }

# Test execution
def run_tests():
    print("=== Alert Processing System Test ===\n")
    
    # Test Case 1: Get recent alerts
    recent_alerts = getAlerts(5, sample_alerts)
    print(f"Test 1 - Recent Alerts: {len(recent_alerts)} alerts retrieved")
    
    # Test Case 2: Filter critical alerts
    critical_alerts = filterCriticalAlerts(sample_alerts)
    print(f"Test 2 - Critical Alerts: {len(critical_alerts)} critical alerts found")
    
    # Test Case 3: Analyze critical alerts
    analysis = analyzeAlerts(critical_alerts)
    print("Test 3 - Critical Alert Analysis:")
    for key, value in analysis.items():
        print(f"  {key}: {value}")
    
    # Bonus: Advanced filtering capabilities
    print(f"\n=== Advanced Analysis ===")
    
    # Group by service
    from collections import defaultdict
    service_groups = defaultdict(list)
    for alert in critical_alerts:
        service_groups[alert['service']].append(alert)
    
    print("Critical alerts by service:")
    for service, alerts in service_groups.items():
        unresolved = sum(1 for a in alerts if not a.get('resolved', True))
        print(f"  {service}: {len(alerts)} total, {unresolved} unresolved")
    
    # Time-based analysis
    critical_timestamps = [datetime.fromisoformat(alert['timestamp'].replace('Z', '+00:00')) 
        for alert in critical_alerts]
    time_span = max(critical_timestamps) - min(critical_timestamps)
    print(f"Critical alerts time span: {time_span}")
    
    return analysis

# Sample alerts data (as provided above)
sample_alerts = [
    {
        "id": "alert_001", "timestamp": "2025-08-29T09:15:00Z", "severity": "critical",
        "service": "database", "message": "Connection pool exhausted", "host": "db-primary-01",
        "metric_value": 100, "metric_type": "connection_count", "tags": ["production", "database"],
        "resolved": False, "acknowledgements": 0
    },
    {
        "id": "alert_002", "timestamp": "2025-08-29T09:20:00Z", "severity": "high",
        "service": "api-gateway", "message": "High response time", "host": "api-01",
        "metric_value": 2500, "metric_type": "response_time_ms", "tags": ["production", "api"],
        "resolved": False, "acknowledgements": 1
    },
    {
        "id": "alert_003", "timestamp": "2025-08-29T09:25:00Z", "severity": "critical",
        "service": "payment-service", "message": "Payment processing failed", "host": "payment-01",
        "metric_value": 15, "metric_type": "error_rate_percent", "tags": ["production", "payment"],
        "resolved": False, "acknowledgements": 3
    },
    {
        "id": "alert_004", "timestamp": "2025-08-29T09:30:00Z", "severity": "medium",
        "service": "user-service", "message": "Memory usage above threshold", "host": "user-01",
        "metric_value": 85, "metric_type": "memory_percentage", "tags": ["production", "backend"],
        "resolved": True, "acknowledgements": 1
    },
    {
        "id": "alert_005", "timestamp": "2025-08-29T09:35:00Z", "severity": "critical",
        "service": "api-gateway", "message": "Service unavailable", "host": "api-02",
        "metric_value": 0, "metric_type": "availability_percent", "tags": ["production", "api"],
        "resolved": False, "acknowledgements": 0
    }
]

if __name__ == "__main__":
    run_tests()