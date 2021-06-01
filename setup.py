#!/usr/bin/python
import os

from setuptools import setup, find_packages

SRC_DIR = os.path.dirname(__file__)
CHANGES_FILE = os.path.join(SRC_DIR, "CHANGES")

with open(CHANGES_FILE) as fil:
    VERSION = fil.readline().split()[0]


setup(
    name="api",
    provides=["api"],
    description="rest api end points to access news data",
    version=VERSION,
    packages=find_packages(exclude=['test']),
    author="abbasmustufain@gmail.com",
    python_requires='>=3.6',
    entry_points={'console_scripts': [
        'api = api:main']},
    include_package_data=True
)
