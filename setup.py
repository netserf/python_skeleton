# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package',
    long_description=readme,
    author='networkserf@gmail.com',
    author_email='networkserf@gmail.com',
    url='https://github.com/netserf/python_skeleton',
    packages=find_packages(exclude=('tests', 'docs'))
)

