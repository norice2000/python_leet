import json


system_metrics = {
    "api-gateway": {
        "cpu": 85,
        "memory": 78,
        "status": "warning",
        "replicas": 3,
        "requests_per_sec": 1250,
        "error_rate": 2.1,
        "uptime_days": 15
    },
    "user-service": {
        "cpu": 45,
        "memory": 62,
        "status": "healthy",
        "replicas": 2,
        "requests_per_sec": 800,
        "error_rate": 0.5,
        "uptime_days": 23
    },
    "payment-service": {
        "cpu": 92,
        "memory": 89,
        "status": "critical",
        "replicas": 1,
        "requests_per_sec": 650,
        "error_rate": 5.2,
        "uptime_days": 8
    },
    "database": {
        "cpu": 67,
        "memory": 81,
        "status": "warning",
        "replicas": 2,
        "requests_per_sec": 0,  # Database doesn't handle HTTP requests
        "error_rate": 1.8,
        "uptime_days": 45
    },
    "redis-cache": {
        "cpu": 34,
        "memory": 45,
        "status": "healthy",
        "replicas": 2,
        "requests_per_sec": 2100,
        "error_rate": 0.1,
        "uptime_days": 32
    },
    "auth-service": {
        "cpu": 78,
        "memory": 85,
        "status": "warning",
        "replicas": 2,
        "requests_per_sec": 420,
        "error_rate": 3.1,
        "uptime_days": 19
    }
}

class StatsMetric():
    def __init__(self):
        self.error_msg = 'invalid'

    def parse(self,metrics):
        try:
            result = self._print_critical(metrics)
            return result
        except Exception as e:
            return e
        
    def _print_critical(self, metrics:dict) -> dict:
        # convert_dict = json.loads(metrics)
        status_counts = 0
        urgent_messages = []
        # status = metrics['status']
        # print(str(status))
        # initalize counter for critical
        for k, v in metrics.items():
            # print(f"k {k}, v: {v}") # k api-gateway, v: {'cpu': 85, 'memory': 78, 'status': 'warning', 'replicas': 3, 'requests_per_sec': 1250, 'error_rate': 2.1, 'uptime_days': 15}
            status = v['status']
            cpu = v['cpu']
            mem = v['memory']
            if status == "critical":
                status_counts += 1
            else:
                status_counts = 1

            if cpu > 80:
                urgent_messages.append(f"{k} CPU is HIGH!")

            if mem > 50:
                urgent_messages.append(f"{k} MEMORY is HIGH!")

        return {
            'service': k,
            'critical' : status_counts,
            'urgent': urgent_messages
        }
        # iterate items for status
        # initalize key status

instantiate = StatsMetric()
result = instantiate.parse(system_metrics)
print(result)