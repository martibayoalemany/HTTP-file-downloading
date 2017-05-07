import exceptions
import unittest

from file_downloader import Constants, Downloader


class test_download(unittest.TestCase):
    def _assertRaises(self, cls, func):
        with self.assertRaises(cls) as context:
            func()
        self.assertTrue(type(context.exception) is context.expected)

    def test_get_target_file_name_for(self):
        self.assertIsNotNone(Constants.get_output_for_url("https://c1.staticflickr.com/11c62358_n.jpg"))
        with self.assertRaises(exceptions.ValueError):
            Constants.get_output_for_url("....asdsa")
        with self.assertRaises(exceptions.ValueError):
            Constants.get_output_for_url(None)

    def test_execute_failed(self):
        with self.assertRaises(ValueError):
            Downloader()._doExecute(None)
        with self.assertRaises(ValueError):
            Downloader()._doExecute([])
        with self.assertRaises(ValueError):
            Downloader()._doExecute("....sd")

