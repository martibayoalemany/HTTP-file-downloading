import codecs
import os
import unittest
import warnings

from file_downloader import *


class test_download(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore")

    def tearDown(self):
        warnings.resetwarnings()

    def test_get_target_file_name_from(self):
        self.assertTrue(Downloader.get_path_from_url("https://c1.staticflickr.com/11c62358_n.jpg"))
        self.assertFalse(Downloader.get_path_from_url("...asdsa"))

    def test_download_failed(self):
        self.assertEquals(Downloader().download([]), 0)
        self.assertEquals(Downloader()._download([]), 0)
        self.assertEquals(Downloader()._download("....sd"), 0)

    def test_download(self):
        initializer = Initializer()
        input_txt = initializer.execute()

        parse_options = lambda: None

        # It downloads the pics with regular http1.1
        if os.path.exists(input_txt):
            with codecs.open(input_txt, "r", "utf-8") as f:
                urls = (line for line in f)
                url = urls.next()
                self.assertEquals(Downloader()._download(url), 1, msg=url)
