#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import passpie_keepass


__version__ = passpie_keepass.__version__


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = []
dependency_links = []
with open('requirements.txt') as _f:
    for _line in _f.readlines():
        _line = _line.strip()
        if _line.startswith('#'):
            pass
        elif _line.startswith('-e') or '://' in _line:
            dependency_links.append(_line)
        else:
            requirements.append(_line)

with open('dev_requirements.txt') as _f:
    dev_requirements = [l for l in (l.strip() for l in _f.readlines()) if l]


setup(
    name='passpie-keepass',
    version=__version__,
    description="Keepass database importer for passpie using kppy",
    long_description=readme + '\n\n' + history,
    author="Constantin Petrisor",
    author_email='costy.petrisor@gmail.com',
    url='https://github.com/costypetrisor/passpie_keepass',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    dependency_links=dependency_links,
    license="MIT",
    keywords='passpie_keepass',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        # 'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Security :: Cryptography',
    ],
    test_suite='tests',
    tests_require=dev_requirements,
    entry_points={
        'passpie_importers': [
            'keepass=passpie_keepass.passpie_keepass:KppyImporter',
        ],
    },
)
