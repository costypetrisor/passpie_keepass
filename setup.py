#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

try:
    from setuptools.command.test import test as TestCommand
    _supports_test_command = True
except ImportError:
    _supports_test_command = False

import passpie_keepass


__version__ = passpie_keepass.__version__


setup_kwargs = {}


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


if _supports_test_command:
    class PyTest(TestCommand):
        user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

        def initialize_options(self):
            TestCommand.initialize_options(self)
            self.pytest_args = []

        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            # import here, cause outside the eggs aren't loaded
            import pytest
            errno = pytest.main(self.pytest_args)
            sys.exit(errno)

    if 'pytest' not in dev_requirements:
        dev_requirements.append('pytest')

    setup_kwargs.setdefault('cmdclass', {}).update(test=PyTest)


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
    **setup_kwargs
)
