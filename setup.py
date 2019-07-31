import os
import re
import glob
import warnings
from setuptools import (setup, find_packages)


class InstallError(Exception):
    """imppload installation error."""
    pass


def version(package):
    """
    :return: the package version as listed in the package `__init.py__`
        `__version__` variable.
    """
    # The version string parser.
    REGEXP = re.compile("""
       __version__   # The version variable
       \s*=\s*       # Assignment
       ['\"]         # Leading quote
       (.+)          # The version string capture group
       ['\"]         # Trailing quote
    """, re.VERBOSE)

    with open(os.path.join(package, '__init__.py')) as f:
       match = REGEXP.search(f.read())
       if not match:
           raise InstallError("The %s __version__ variable was not found" %
                              package)
       return match.group(1)


def requires():
    with open('requirements.txt') as f:
        return f.read().splitlines()


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name = 'immpload',
    version = version('immpload'),
    author = 'OHSU Knight Cancer Institute',
    author_email = 'loneyf@ohsu.edu',
    platforms = 'Any',
    license = 'MIT',
    keywords = 'Immpload',
    packages = find_packages(exclude=['test**']),
    package_data = dict(immpload=['conf/*.cfg']),
    scripts = glob.glob('bin/*'),
    url = 'http://immpload.readthedocs.org/en/latest/',
    description = 'Immport upload package',
    long_description = readme(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    install_requires = requires(),
)
