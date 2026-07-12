import subprocess

def driver():
    interfaces = subprocess.check_output(
        "netsh interface show interface",
        shell=True
        ).decode("utf-8", errors="ignore")

    drivers = subprocess.check_output(
        "driverquery",
        shell=True
        ).decode("utf-8", errors="ignore")

    print(interfaces)
    print(drivers)

    