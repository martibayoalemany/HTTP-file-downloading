#!/usr/bin/env python

from setuptools import setup, find_packages
import unittest


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    return test_suite


setup(name='george_rowberry_python',
      version='1.0',
      description='Snippets',
      author='Marti Bayo Alemany',
      author_email='martibayoalemany@grafai.com',
      url='http://grafai.com',
      packages=find_packages(),
      test_suite='setup.my_test_suite'
      )

