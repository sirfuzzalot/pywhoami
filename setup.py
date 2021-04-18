import sys

from setuptools import setup

if sys.version_info < (3, 8, 0):
    sys.exit("Python 3.8.0+ Required")

setup()
