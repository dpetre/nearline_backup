from setuptools import setup, find_packages
setup(
    name="NearlineBackup",
    version="0.1",
    description="Manages backup and Goole Nearline sync",
    packages=find_packages(),
    install_requires=["gsutil > 4", "pyyaml"],
    entry_points={
        'console_scripts': [
            'nearline_backup = modules.__main__:main',
        ]
    }
)
