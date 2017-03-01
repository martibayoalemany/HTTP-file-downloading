import sys, os

filePath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, filePath + '/file_downloader')


class Paths:
    def __init__(self):
        pass

    @staticmethod
    def get_downloads_abspath():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../downloads")

    @staticmethod
    def get_downloads_urlspath():
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../downloads/inputs_urls.txt")