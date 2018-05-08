"""setup for cryptoconfig
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cryptoconfig',
    version='1.0.0',
    description='Python class for handling encrypted elements in a config file.  Extension of ConfigParser.',
    long_description = long_description,
    author='NREL',
    author_email='david.martin@nrel.gov',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=['configparser', 'cryptography'],
    python_requires='>=3',
    scripts=['bin/cryptocfg.py']
)