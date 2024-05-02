import os

"""
Get a list of valid Python files to import as modules.
Uses the location of __file__ to identify the folder.
"""

list_of_files = [file for file in os.listdir(os.path.dirname(__file__))  
                 # Get the list of files in the directory
                 if not file.startswith('-')  
                 # Exclude files starting with '-'
                 and not file.startswith('.')  
                 # Exclude hidden files starting with '.'
                 and file.endswith('.py')  
                 # Include only files ending with '.py'
                 and os.path.isfile(os.path.join(os.path.dirname(__file__), file))]
                 # Check if it's a file

module_list = []

# Drop the .py extension from the file list and populate the module_list
for name in list_of_files:
    module_list.append(os.path.splitext(name)[0])
    # Remove the '.py' extension and add to module_list

# Use the generated module_list for wildcard imports
__all__ = module_list  
# Expose all modules for wildcard imports
