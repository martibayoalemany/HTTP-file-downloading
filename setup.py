#!/usr/bin/env python27
# pylint: skip-file
from setuptools import setup, find_packages
import unittest
import sys


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('src/.', pattern='test_*.py')
    return test_suite


if __name__ == '__main__':

    if sys.version_info > (3, 0):
        warnings.warn(
            "The implementation was not checked against Python 3.5")

    setup(name='python-file-downloader',
          test_suite='setup.my_test_suite',
          version='1.0.0',
          description='python ag test',
          url='http://graphai.co',
          author='Marti Bayo Alemany',
          author_email='martibayoalemany@gmail.com',
          license='MIT',
          #packages=find_packages(),
          packages=['src/file_downloader'],
          entry_points={
              'disutils.commands': [
                  'py_reqs = file_downloader:PyReqs'
              ]

          },
          install_requires=[
              'asyncio==3.4.3',
              'autopep8==1.3.2',
              'BeautifulSoup==3.2.1',
              'beautifulsoup4==4.6.0',
              'bs4==0.0.1',
              'enum34==1.1.6',
              'h2==2.6.2',
              'hpack==3.0.0',
              'html5lib==0.999999999',
              'hyper==0.7.0',
              'hyperframe==3.2.0',
              'mechanize==0.3.3',
              'pkg-resources==0.0.0',
              'pycodestyle==2.3.1',
              'six==1.10.0',
              'webencodings==0.5.1', '']
          )
