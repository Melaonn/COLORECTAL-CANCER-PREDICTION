from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-Colorectal",
    version="0.1",
    author="Melson",
    packages=find_packages(),
    install_requires = requirements,
)