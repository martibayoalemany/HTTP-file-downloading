# pylint: skip-file
import unittest
import os
import sys

sys.path.append(os.path.realpath(os.getcwd() + '/..'))
from file_downloader import Constants

class TestConstants(unittest.TestCase):

    def test_get_output_for_url(self):
        self.assertIsNotNone(Constants.get_output_for_url(
            "https://address/resources"))

        with self.assertRaises(ValueError):
            Constants.get_output_for_url("....asdsa")
        with self.assertRaises(ValueError):
            Constants.get_output_for_url(None)

    def test_load_links(self):
        """
            Loads 10 links 
        """
        self.assertEqual(10, len(Constants.load_links(10)))
