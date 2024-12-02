from setuptools import setup, find_packages

"""
setup.py fo dev-cli

This script is used to package and distribute the zap-cli project.
It includes details like the package name, version, dependencies, 
and entry points, making it easy to install and use as a command-line tool.

Key features of this setup.py file:
- Defines the package name and version.
- Lists required dependencies (like the Click library).
- Specifies the command-line entry point, allowing the 'zap-cli' command to be used in the terminal.
- Enables installation in development mode (editable mode) with `pip install -e .`.

Running `python setup.py install` or `pip install -e .` allows users to install 
the zap-cli package and make the zap-cli command available globally.

This file should be included in version control (e.g., Git) since it is essential for 
package installation and distribution, but the generated `*.egg-info/` directories 
should be excluded from version control.
"""

setup(
    name='zap-cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'zap-cli=zap_cli:cli',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
