# pylint: skip-file
import unittest
from file_downloader import Constants
from file_downloader.downloader import download


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
