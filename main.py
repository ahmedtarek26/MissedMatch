import os
import subprocess

def install_packages():
    # Install packages from requirements.txt
    subprocess.call(["pip", "install", "-r", "requirements.txt"])
    # subprocess.run(["python", "-m", "mlflow", "ui"])


def run_scripts():
    # Run the first Python script
    subprocess.call(["python", "src/train.py"])

if __name__ == "__main__":
    install_packages()
    run_scripts()