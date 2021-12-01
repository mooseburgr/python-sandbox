# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name="python-sandbox",
    version="0.0.1",
    description="A pip package",
    license="MIT",
    author="Kyle Johnson",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
    ],
    project_urls = {
        "Bug Tracker": "https://github.com/mooseburgr/python-sandbox/issues"
    },
    url='https://github.com/mooseburgr/python-sandbox',
)
