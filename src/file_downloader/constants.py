import sys
import os
import urlparse

filePath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, filePath + '/file_downloader')


# noinspection PyClassHasNoInit
class Constants(object):
    @classmethod
    def get_downloads_abspath(cls):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../downloads")

    @classmethod
    def get_downloads_urlspath(cls):
        """
         Path to a file which contain urls
        """
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../downloads/inputs_urls.txt")

    @classmethod
    def get_urls(cls):
        """
            Urls with pages to pics
        """
        return ["https://goo.gl/W0cMUf",
                "https://goo.gl/oDi4jg",
                "https://goo.gl/qBcMct",
                "https://goo.gl/9MbBMk",
                "https://goo.gl/Kr0nmT",
                "https://goo.gl/MDTzh8"]

    @classmethod
    def get_path_for_url(cls, url):
        """
            - It maps a url to the downloads abs path
        """
        if not urlparse.urlparse(url).scheme:
            return None
        target_file = urlparse.urlsplit(url).path.split("/")[-1]
        if target_file is not None:
            return os.path.join(cls.get_downloads_abspath(), target_file.rstrip())
        else:
            return None