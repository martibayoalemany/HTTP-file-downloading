""" Test for the download api """
# pylint: skip-file
imports_succeeded = True
try:
    import exceptions
    import unittest
    import sys
    import os
    sys.path.append(os.path.realpath(os.getcwd() + '/..'))
    from file_downloader import Constants, download, download_parallel
except ImportError as e:
    imports_succeeded = False

if imports_succeeded:
    class TestDownloader(unittest.TestCase):
        """ It checks whether we can download several images with 2,4,7 and 16 processes """

        def test_parameters(self):
            """ parameters check """
            self.assertFalse(download(None)[0])
            self.assertFalse(download([])[0])
            self.assertFalse(download(".....sd")[0])

        def test_download_failed(self):
            """ Download a non existing image """
            with self.assertRaises(exceptions.OSError):
                download_parallel(links=["https://not_existing_url"])

        def test_parallelization(self):
            """ Download 8 links with multiple processes """
            self.do_parallel_download(Constants.load_links(8), serialize=False)

        def test_parallelization_serialize(self):
            """ Download 8 links with multiple processes and serialization """
            self.do_parallel_download(Constants.load_links(8), serialize=True)

        def do_parallel_download(self, links, serialize):
            Constants.picture_serialization = serialize
            for num in [2, 4, 7, 16]:
                download_parallel(links=links, num_processes=num)

            print("Repeting download")
            for num in [2, 4, 7, 16]:
                download_parallel(links=links, num_processes=num)

        #@unittest.skip("long runner")
        def test_parallelization_long(self):
            links = Constants.load_links()
            for num in [2, 4, 7, 16]:
                download_parallel(links=links, num_processes=num)
