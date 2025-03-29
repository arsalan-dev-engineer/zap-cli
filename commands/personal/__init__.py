import os

def get_python_modules(path):
    """
    Recursively get a list of valid Python files to import as modules.
    """
    module_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if not file.startswith('-') and not file.startswith('.') and file.endswith('.py'):
                # Exclude files starting with '-' and '.'
                # Include only Python files ending with '.py'
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    # If it's a file, add it to the module list without the '.py' extension
                    module_list.append(os.path.splitext(os.path.relpath(file_path, start=path))[0].replace(os.sep, '.'))
    return module_list

# Get the directory where this __init__.py is located
directory = os.path.dirname(__file__)

# Get the list of Python modules in the current directory and subdirectories
module_list = get_python_modules(directory)

# Use the generated module list for wildcard imports
__all__ = module_list
