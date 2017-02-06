import unittest
import warnings

from downloader import Downloader


class test_download(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore")

    def tearDown(self):
        warnings.resetwarnings()

    def test_get_target_file_name_from(self):
        self.assertTrue(Downloader.get_path_from_url("https://c1.staticflickr.com/11c62358_n.jpg"))
        self.assertFalse(Downloader.get_path_from_url("...asdsa"))

    def test_download(self):
        self.assertEquals(Downloader().download([]), 0)
        self.assertEquals(Downloader()._download([]), 0)
        self.assertEquals(Downloader()._download("....sd"), 0)
        self.assertEquals(Downloader()._download("https://c1.staticflickr.com/1/134/358870878_8811c62358_n.jpg"), 1)
