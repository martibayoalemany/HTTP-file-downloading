import multiprocessing
import os
import six
import urlparse

import itertools

import time

from mechanize import Request, urlopen, HTTPError, URLError

from paths import Paths


class Downloader:
    def __init__(self):
        pass

    @staticmethod
    def get_path_from_url(url):
        """
            - It maps urls to a local folder for later download
        """
        if not urlparse.urlparse(url).scheme:
            return None
        target_file = urlparse.urlsplit(url).path.split("/")[-1]
        if target_file is not None:
            return os.path.join(Paths.get_downloads_abspath(), target_file.rstrip())
        else:
            return None

    def download(self, urls, processes=1):
        if urls is None or not isinstance(urls, list) or len(urls) == 0:
            return 0
        start = time.time()
        chunks = itertools.tee(urls, processes)
        processes = []
        for chunk in chunks:
            p = multiprocessing.Process(target=lambda x: [self._download(url) for url in x], args={chunk})
            processes.append(p)
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        print("Download with {} processes took {}".format(processes, (time.time() - start)))

    @staticmethod
    def _download(url):
        """
            - it downloads one url at a time and stores the content into the download folder
        """
        try:
            if url is None or not isinstance(url, six.types.StringTypes):
                return 0
            target_file_name = Downloader.get_path_from_url(url)
            if target_file_name is None:
                return 0
            # TODO: change urllib2 for Hyper library for HTTP2 support
            req = Request(url)
            web_file = urlopen(req)
            with open(target_file_name, "wb") as f:
                f.write(web_file.read())
        except HTTPError, e:
            print "HTTPError:", e.code, url
            return 0
        except URLError, e:
            print "URLError:", e.reason, url
            return 0
        except IOError, e:
            print "IOError:", e.message, url
            return 0
        except ValueError, e:
            print "ValueError:", e.message, url
            return 0
        return 1
