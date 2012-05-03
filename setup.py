#!/usr/bin/env python
"""
Gearbox
======

Gearbox is an application bootstrapper for OpenShift.

You can use it to bootstrap pre-built applications on OpenShift.

:copyright: (c) 2012 by the Evan Hazlett
:license: Apache Software License version 2.0, see LICENSE for more details.
"""

from setuptools import setup, find_packages
import gearbox

install_requires = [
    'requests>=0.11.2',
    'simplejson>=2.5.0',
]

setup(
    name='gearbox',
    version=gearbox.__version__,
    author='Evan Hazlett',
    author_email='ejhazlett@gmail.com',
    url='http://github.com/ehazlett/gearbox',
    description='OpenShift application bootstrapper.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    zip_safe=False,
    install_requires=install_requires,
    license='Apache Software License',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'gb = gearbox.cli:main',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)