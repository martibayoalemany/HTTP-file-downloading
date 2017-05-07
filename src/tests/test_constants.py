import exceptions
import unittest

from file_downloader import Constants
from file_downloader.downloader import _doExecute, download


class test_constants(unittest.TestCase):

    def test_get_target_file_name_for(self):
        self.assertIsNotNone(Constants.get_output_for_url("https://c1.staticflickr.com/11c62358_n.jpg"))
        with self.assertRaises(exceptions.ValueError):
            Constants.get_output_for_url("....asdsa")
        with self.assertRaises(exceptions.ValueError):
            Constants.get_output_for_url(None)

    def test_load_links(self):
        self.assertEqual(10, len(Constants.load_links(10)))

