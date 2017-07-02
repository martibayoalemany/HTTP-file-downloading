#!/usr/bin/env python
# pylint: skip-file
from setuptools import setup, find_packages
import unittest
import sys
import warnings
import os

if sys.version_info < (2, 7):
    raise SystemExit('file_downloader requires python >= 2.7')

if sys.version_info.major > 2:
    raise SystemExit('file_downloader only works on python 2.x')
 
sys.path.insert(0, os.getcwd())

CLASSIFIERS = """\
Natural Language :: English
Operating System :: Linux
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.7
Topic :: Internet :: WWW/HTTP
Topic :: Software Development :: Libraries
"""

def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    return test_suite


if __name__ == '__main__':


    setup(name='file_downloader',
          test_suite='setup.my_test_suite',
          version='1.0.0',
          description='Checking libraries for file downloading',
          url='https://pypi.python.org/pypi/file-downloader',
          author='Marti Bayo Alemany',
          author_email='martibayoalemany@grafai.com',
          classifiers=[c for c in CLASSIFIERS.split("\n") if c],
          license='MIT',
          package_data={
              'docs': ['README.md']
          },
          cmdclass={
              'pyreqs': 'file_downloader:PyReqs'
          },
          packages=find_packages(),
          entry_points={
              'disutils.commands': [
                  'py_reqs = file_downloader:PyReqs'
              ]

          },
          install_requires=[
          ]

          )
