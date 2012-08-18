#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = __import__('djutils').__version__

setup(
    name="djutils",
    version=VERSION,
    author='Siddharth Doshi',
    author_email='scdoshi@gmail.com',
    description=("Basic Utilities for Django Projects"),
    packages=find_packages(),
    url="http://github.com/scdoshi/djutils/",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
