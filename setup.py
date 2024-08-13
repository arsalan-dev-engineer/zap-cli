from setuptools import setup, find_packages

"""
setup.py for azzy-cli

This script is used for packaging and distributing the azzy-cli project.
It includes configuration details such as the package name, version, dependencies,
and entry points, making it possible to install the package and use it as a command-line
tool.

Key functions of this setup.py file:
- Defines the package name and version.
- Lists the required dependencies (e.g., Click library).
- Specifies the command-line entry point, allowing the 'azzy-cli' command to be used in the terminal.
- Facilitates installation of the package in development mode (editable mode) using `pip install -e .`.

By running `python setup.py install` or `pip install -e .`, this script enables users to install 
the azzy-cli package and makes the azzy-cli command globally available on their system.

This file should be included in your version control (e.g., Git) as it is essential for package
installation and distribution, but directories like `*.egg-info/` generated during the installation process
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
