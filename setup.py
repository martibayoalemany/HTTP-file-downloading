#!/usr/bin/env python

from setuptools import setup, find_packages
import unittest


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    return test_suite


setup(name='file_downloader',
      version='1.0',
      description='job entry test requirement',
      author='Marti Bayo Alemany',
      author_email='martibayoalemany@gmail.com',
      url='http://graphai.co',
      packages=find_packages(),
      test_suite='setup.my_test_suite'
      )

