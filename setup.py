#!/usr/bin/env python3

from setuptools import setup

with open('requirements.txt') as f:
    requirements = [L for L in f.read().splitlines() if not L.startswith('#')]

version = '0.3.2'

setup(
    name='yatardiff',
    version=version,
    install_requires=requirements,
    author='Toshihiro Kamiya',
    author_email='kamiya@mgj.nifty.com',
    scripts=['yatardiff'],
    url='https://github.com/tos-kamiya/yatardiff/',
    license='Public Domain',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Operating System :: POSIX",
        "Topic :: Utilities",
    ],
    description='Run command with giving parameters incrementally',
)

