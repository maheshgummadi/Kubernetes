import json
import os


class SREController:

    def __init__(self, metrics_file):
        self.metrics_file = metrics_file

    def load_metrics(self):

        with open(self.metrics_file, 'r') as f:
            return json.load(f)

    def evaluate_slo(self, data):

        metrics = data["metrics"]
        slo = data["slo"]
        error_budget = data["error_budget"]

        violations = []

        if metrics["availability"] < slo["availability_target"]:
            violations.append("availability_breach")

        if metrics["latency_ms"] > slo["latency_threshold_ms"]:
            violations.append("latency_breach")

        return violations, error_budget

    def decision_engine(self, violations, error_budget):

        burn_rate = error_budget["burn_rate"]

        print("\n===== SRE DECISION ENGINE =====")
        print(f"Violations: {violations}")
        print(f"Burn Rate: {burn_rate}")

        if burn_rate > 2.5:
            return "ROLLBACK"

        elif "latency_breach" in violations:
            return "SCALE"

        elif len(violations) == 0:
            return "NO_ACTION"

        else:
            return "MONITOR"

    def execute_action(self, action):

        print(f"\nExecuting Action: {action}")

    

        if action == "ROLLBACK":
            print("[SIMULATION] Kubernetes Rollback executed successfully")

        elif action == "SCALE":
            print("[SIMULATION] Kubernetes Scaling to 4 replicas executed")

        elif action == "MONITOR":
            print("[SIMULATION] System under observation...")

        elif action == "NO_ACTION":
            print("[SIMULATION] System stable. No remediation required.")

    def run(self):

        print("Controller started successfully")

        data = self.load_metrics()

        violations, error_budget = self.evaluate_slo(data)

        action = self.decision_engine(violations, error_budget)

        self.execute_action(action)


# ---------------- MAIN EXECUTION ---------------- #

if __name__ == "__main__":

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    metrics_path = os.path.join(base_dir, "monitoring", "metrics.json")

    controller = SREController(metrics_path)
    controller.run()