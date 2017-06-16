import exceptions
import unittest

from file_downloader import Constants
from file_downloader.downloader import doDownload, download


class test_download(unittest.TestCase):
    """
       It checks whether we can download several images with 2,4,7 and 16 processes
    """

    def test_execute_failed(self):
        """
            Thest fails for this parameters to _doExecute
        """
        self.assertFalse(doDownload(None)[0])
        self.assertFalse(doDownload([])[0])
        self.assertFalse(doDownload(".....sd")[0])

    def test_download_image_failed(self):
        """
            Download a non existing image
        """
        with self.assertRaises(exceptions.OSError):
            download(links=["https://c1.staticflickr.com/11c62358_n.jpg"])

    def test_speed(self):
        """
            Download 100 links with multiple processes
        """
        Constants.picture_serialization = False
        links = Constants.load_links(100)
        for num in [2, 4, 7, 16]:
            download(links=links, num_processes=num)
        for num in [2, 4, 7, 16]:
            download(links=links, num_processes=num)

