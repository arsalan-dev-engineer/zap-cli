from setuptools import setup, find_packages

setup(
    name="zap-cli",
    version="0.1",
    packages=find_packages(),  # Automatically finds the zap_cli package
    install_requires=[
        'click',  # Add any dependencies here, like 'requests', etc.
    ],
    entry_points={
        'console_scripts': [
            'zap-cli = zap_cli.zap_cli:cli',  # Correct the path to the cli function
        ],
    },
)
