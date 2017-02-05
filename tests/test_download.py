import unittest
import warnings


class test_download(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings("ignore")

    def tearDown(self):
        warnings.resetwarnings()

