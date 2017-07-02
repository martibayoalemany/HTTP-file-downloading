# pylint: skip-file
"""
 Test for the download api
"""
import exceptions
import unittest

from file_downloader import Constants, download, download_parallel


class TestDownloader(unittest.TestCase):
    """
       It checks whether we can download several images with 2,4,7 and 16 processes
    """

    def test_parameters(self):
        """
            parameters check
        """
        self.assertFalse(download(None)[0])
        self.assertFalse(download([])[0])
        self.assertFalse(download(".....sd")[0])

    def test_download_failed(self):
        """
            Download a non existing image
        """
        with self.assertRaises(exceptions.OSError):
            download_parallel(links=["https://not_existing_url"])

    def test_parallelization(self):
        """
            Download 100 links with multiple processes
        """
        Constants.picture_serialization = False
        links = Constants.load_links(100)
        for num in [2, 4, 7, 16]:
            download_parallel(links=links, num_processes=num)
        for num in [2, 4, 7, 16]:
            download_parallel(links=links, num_processes=num)
