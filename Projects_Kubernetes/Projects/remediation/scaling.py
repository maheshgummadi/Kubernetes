import subprocess


def scale_up():

    print("Triggering autoscaling policy...")

    subprocess.run([
        "kubectl",
        "scale",
        "deployment",
        "sre-microservice",
        "--replicas=5"
    ])

    print("Scaling completed based on latency breach")