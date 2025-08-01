#!/usr/bin/env python3

import subprocess
import sys
import importlib

def is_package_installed(import_name):
    """
    Check if a Python package can be imported (i.e., is installed).
    """
    try:
        importlib.import_module(import_name)
        return True
    except ImportError:
        return False

def install_requirements(file='requirements.txt'):
    """
    Install packages listed in the requirements.txt file if not already installed.
    Works inside a virtual environment on Ubuntu.
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]

        to_install = []

        for package in lines:
            # Extract the module name from the package spec if needed
            # e.g., 'pandas==1.5.3' -> 'pandas'
            module_name = package.split('==')[0].strip()
            if not is_package_installed(module_name):
                print(f"📦 {package} is NOT installed. Marked for installation.")
                to_install.append(package)
            else:
                print(f"✅ {package} is already installed.")

        if to_install:
            print(f"\n➡ Installing missing packages: {to_install}\n")
            subprocess.check_call([sys.executable, "-m", "pip", "install", *to_install])
            print("\n✅ All missing packages installed successfully.")
        else:
            print("\n🎉 All required packages are already installed.")

    except FileNotFoundError:
        print(f"❌ The file '{file}' was not found.")
    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred during installation:\n{e}")

if __name__ == "__main__":
    # Optional: check if running in a virtual environment
    if sys.prefix == sys.base_prefix:
        print("⚠️ WARNING: You are not in a virtual environment!")
    install_requirements()

