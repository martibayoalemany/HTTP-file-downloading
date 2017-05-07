import exceptions
import unittest

from file_downloader import Constants
from file_downloader.downloader_hyper import _doExecute, download


class test_download_hyper(unittest.TestCase):

    def test_execute_failed(self):
        self.assertFalse(_doExecute(None)[0])
        self.assertFalse(_doExecute([])[0])
        self.assertFalse(_doExecute(".....sd")[0])

    def test_download_image_failed(self):
        with self.assertRaises(exceptions.OSError):
            download(links=["https://c1.staticflickr.com/11c62358_n.jpg"])

    @unittest.skip("test skipping")
    def test_speed(self):
        Constants.picture_serialization = False
        links = Constants.load_links(100)
        for num in [2,4,7,16]:
            download(links=links, num_processes=num)
        for num in [2,4,7,16]:
            download(links=links, num_processes=num)
