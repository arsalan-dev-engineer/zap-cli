from setuptools import setup, find_packages

# ------------------------------------------------------------------------
# This is the setup.py file for the zap-cli package.
# It is used for packaging and distributing the zap-cli command-line tool.
# It defines the metadata and configuration for the package, including:
# - The package name, version, and dependencies.
# - The entry point for the command-line tool.
# - It also specifies the modules or packages that should be included
#   in the distribution (using find_packages).
# ------------------------------------------------------------------------

setup(
    # Name of the package (this is what will be used for installation)
    name="zap-cli",

    # Version of the package (helps in managing versions and dependencies)
    version="0.1",

    # Automatically discover and include all Python packages in the zap_cli directory
    # Finds and includes all packages in the zap_cli module
    packages=find_packages(),

    # List of dependencies that should be installed when the package is installed
    install_requires=[
        # Required for building the command-line interface with Click
        'click',
        # Add any other external dependencies here (e.g., 'requests', 'flask', etc.)
    ],

    # Entry points for creating executable commands via the command line
    entry_points={
        'console_scripts': [
            # This defines a command called 'zap-cli' that runs the cli() function
            # from the zap_cli.zap_cli module (your main CLI script)
            # Points to the `cli` function in `zap_cli/zap_cli.py`
            'zap-cli = zap_cli.zap_cli:cli',
        ],
    },
)
