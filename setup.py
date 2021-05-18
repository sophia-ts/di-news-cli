#!/usr/bin/env python

from setuptools import setup

setup(
    name='di-news-cli',
    version='1.0',
    description='Later',
    author='Sophia Tsivoula',
    author_email='p18tsiv@ionio.gr',
    scripts=['di-news-cli'],
    url='https://github.com/sophia-ts/di-news-cli',
    python_requires='>=3',
    install_requires=[
    'bs4',
    'requests',
  ],
)