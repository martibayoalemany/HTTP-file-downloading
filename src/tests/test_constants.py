# pylint: skip-file
import unittest
from file_downloader import Constants
from file_downloader.downloader import _doExecute, download


class test_constants(unittest.TestCase):
    """
        class for :file_downloader.Constants:
    """

    def test_get_target_file_name_for(self):
        """
            :test_get_target_file_name_for:
            It checks that :Constants.get_output_for_url: delivers ValueError
            in case the parameter url is not an url
        """
        self.assertIsNotNone(Constants.get_output_for_url(
            "https://c1.staticflickr.com/11c62358_n.jpg"))
        with self.assertRaises(ValueError):
            Constants.get_output_for_url("....asdsa")
        with self.assertRaises(ValueError):
            Constants.get_output_for_url(None)

    def test_load_links(self):
        """
            Loads 10 links 
        """
        self.assertEqual(10, len(Constants.load_links(10)))
