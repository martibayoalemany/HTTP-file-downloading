import exceptions
import unittest

from file_downloader import Constants
from file_downloader.downloader import _doExecute, download


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

    def test_load_links(self):
        self.assertEqual(10, len(Constants.load_links(10)))

    def test_execute_failed(self):
        self.assertFalse(_doExecute(None)[0])
        self.assertFalse(_doExecute([])[0])
        self.assertFalse(_doExecute(".....sd")[0])

    def test_download_image_failed(self):
        with self.assertRaises(exceptions.OSError):
            download(links=["https://c1.staticflickr.com/11c62358_n.jpg"])

    def test_speed(self):
        Constants.remove_output_dir()
        download(max_links=100, num_processes=2)

        Constants.remove_output_dir()
        download(max_links=100, num_processes=20)

        Constants.remove_output_dir()
        download(max_links=100, num_processes=30)

        Constants.remove_output_dir()
        download(max_links=100, num_processes=40)

        Constants.remove_output_dir()
        download(max_links=100, num_processes=50)
