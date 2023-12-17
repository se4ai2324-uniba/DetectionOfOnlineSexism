"""
Module: setup
Description: This module specifies metadata about the project,
including its name, packages, version, description, author and license.
Authors: Francesco Brescia
        Maria Elena Zaza
        Grazia Perna
"""
from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='A model used for detection of online sexism.',
    author='Ugur Turhan',
    license='MIT',
)
