from setuptools import setup, find_packages

"""
setup.py for azzy-cli

This script is used to package and distribute the azzy-cli project.
It includes details like the package name, version, dependencies, 
and entry points, making it easy to install and use as a command-line tool.

Key features of this setup.py file:
- Defines the package name and version.
- Lists required dependencies (like the Click library).
- Specifies the command-line entry point, allowing the 'azzy-cli' command to be used in the terminal.
- Enables installation in development mode (editable mode) with `pip install -e .`.

Running `python setup.py install` or `pip install -e .` allows users to install 
the azzy-cli package and make the azzy-cli command available globally.

This file should be included in version control (e.g., Git) since it is essential for 
package installation and distribution, but the generated `*.egg-info/` directories 
should be excluded from version control.
"""


setup(
    # package name
    name='azzy-cli',
    # package version
    version='0.1',
    # automatically find and include all packages
    packages=find_packages(),
    # include other files listed in MANIFEST.in
    include_package_data=True,
    install_requires=[
        # add any other dependencies your CLI needs
        'click',  
    ],
    entry_points={
        'console_scripts': [
            # expose azzy-cli as a command
            'azzy-cli=azzy_cli:cli',
            # add other cli's here.
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
