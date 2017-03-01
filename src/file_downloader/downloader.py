from mechanize import Request, urlopen, HTTPError, URLError, Browser
from constants import Constants

import os
import six
import time
import bs4
import codecs
import itertools
import multiprocessing


class Downloader:
    def __init__(self, output_txt=Constants.get_downloads_urlspath()):
        self.output_txt = output_txt
        self.links = list()

    def load_links(self):
        soup = None
        if not os.path.exists(self.output_txt):
            for url in Constants.get_urls():
                try:
                    br = Browser()
                    br.set_handle_robots(False)
                    soup = bs4.BeautifulSoup(br.open(url).read(), "html.parser")
                    pics = soup.find_all("img")
                    pics = (pic["src"] for pic in pics if pic.attrs.has_key("src"))
                    with codecs.open(self.output_txt, "w", "utf-8") as f:
                        for pic in pics:
                            f.write("{}\n".format(pic))
                            self.links.append(pic)
                except Exception as e:
                    print("_init_url:", e)
                finally:
                    # it frees memory to prevent a memory leak if the html file was a large one
                    if soup is not None:
                        soup.decompose()
                print("init urls for input file {} with {} pics".format(url, len(self.links)))
        elif len(self.links) == 0:
            with codecs.open(self.output_txt, 'r', 'utf-8') as input:
                self.links.append(input.readlines())

    def execute(self, processes=1):
        if not isinstance(self.links, six.types.ListType) or self.links is None:
            raise Exception("links is not initialized to a list")
        if not len(self.links):
            self.load_links()
        start = time.time()
        chunks = itertools.tee(self.links, processes)
        processes = []
        for chunk in chunks:
            p = multiprocessing.Process(target=lambda x: [self._execute(url[0]) for url in x], args={chunk})
            processes.append(p)
        for p in processes:
            p.start()
        for p in processes:
            p.join()
        print("Download with {} processes took {}".format(processes, (time.time() - start)))

    @staticmethod
    def _execute(url):
        """
            - it downloads one url at a time and stores the content into the download folder
        """
        try:
            if url is None or not isinstance(url, six.types.StringTypes):
                return 0
            target_file_name = Constants.get_path_for_url(url)
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


if __name__ == '__main__':
    Downloader().execute()
