import json
import os

# Ensure correct path (absolute-safe)
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
metrics_path = os.path.join(base_dir, "monitoring", "metrics.json")

failure_metrics = {
    "service": "sre-microservice",
    "slo": {
        "availability_target": 99.0,
        "latency_threshold_ms": 300
    },
    "metrics": {
        "availability": 91.0,
        "latency_ms": 650,
        "error_rate": 12
    },
    "error_budget": {
        "total_budget": 100,
        "consumed": 85,
        "burn_rate": 3.5
    }
}

with open(metrics_path, 'w') as file:
    json.dump(failure_metrics, file, indent=4)

print("Failure simulation completed successfully")