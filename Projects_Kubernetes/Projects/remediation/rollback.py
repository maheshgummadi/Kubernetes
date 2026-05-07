import subprocess


def rollback():

    print("Initiating reliability-based rollback...")

    subprocess.run([
        "kubectl",
        "rollout",
        "undo",
        "deployment",
        "sre-microservice"
    ])

    print("Rollback executed successfully")