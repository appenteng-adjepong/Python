import subprocess
import sys
import importlib

def is_package_installed(import_name):
    """
    Checks if a package is installed by trying to import it.
    """
    try:
        importlib.import_module(import_name)
        return True
    except ImportError:
        return False

def install_requirements(file='requirements.txt'):

    try:
        with open(file, "r", encoding="utf8",) as f:
                lines = [text.rstrip("\n") for text in f.readlines()]

        to_install = []
        for line in lines:
            if not is_package_installed(line):
                print(f"📦 {line} is NOT installed. Marked for installation.")
                to_install.append(line)
            else:
                print(f"✅ {line} is already installed.")

        if to_install:
            print(f"\n➡ Installing missing packages: {to_install}\n")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', *to_install])
            print("\n✅ All missing packages installed successfully.")
        else:
            print("\n🎉 All required packages are already installed.")

    except FileNotFoundError:
        print(f"❌ The file '{file}' was not found.")
    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred while installing packages:\n{e}")

if __name__ == '__main__':
    install_requirements()
