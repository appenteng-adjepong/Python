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
    
print(is_package_installed("scikit-learn"))