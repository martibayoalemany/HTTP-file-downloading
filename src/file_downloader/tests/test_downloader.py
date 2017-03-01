import unittest

from file_downloader import *


class test_download(unittest.TestCase):

    def test_get_target_file_name_for(self):
        self.assertTrue(Constants.get_path_for_url("https://c1.staticflickr.com/11c62358_n.jpg"))
        self.assertFalse(Constants.get_path_for_url("...asdsa"))

    def test_execute(self):
        self.failIfEqual(Downloader().execute(), 0)

    def test_execute_failed(self):
        self.assertEquals(Downloader()._execute([]), 0)
        self.assertEquals(Downloader()._execute([]), 0)
        self.assertEquals(Downloader()._execute("....sd"), 0)


