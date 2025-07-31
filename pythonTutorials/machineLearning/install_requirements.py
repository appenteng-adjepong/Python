import sys
import importlib
import subprocess

def is_package_installed(import_name):
    """
    Checks if a package is installed by trying to import it.
    """
    try:
        importlib.import_module(import_name)
        return True
    except ImportError:
        return False

def install_requirements(file: str = 'requirements.txt') -> None:
    """
    Installs packages listed in the given requirements file using pip.

    Parameters:
    - file (str): Path to the requirements file. Defaults to 'requirements.txt'.
    """
    try:
        with open(file, "r", encoding="utf8",) as f:
            lines = [text.rstrip("\n") for text in f.readlines()]

        to_install = []
        known_import_map = {
                'scikit-learn': 'sklearn',
                'Pillow': 'PIL',
                'PyYAML': 'yaml',
                'python-dateutil': 'dateutil',
            }
        for package in lines:
            if known_import_map.get(package):
                package = known_import_map[package]
            if not is_package_installed(package):
                print(f"📦 {package} is NOT installed. Marked for installation.")
                to_install.append(package)
            else:
                print(f"✅ {package} is already installed.")

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
