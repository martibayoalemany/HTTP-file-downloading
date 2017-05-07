import os
import sys
import urlparse

import bs4
import exceptions
import six
from mechanize import Browser

filePath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, filePath + '/file_downloader')


# noinspection PyClassHasNoInit
class Constants(object):
    @classmethod
    def load_links(cls):
        """        
        :return: a list of urls that link to images 
        """
        links = list()
        soup = None
        for url in ["https://goo.gl/W0cMUf",
                    "https://goo.gl/oDi4jg",
                    "https://goo.gl/qBcMct",
                    "https://goo.gl/9MbBMk",
                    "https://goo.gl/Kr0nmT",
                    "https://goo.gl/MDTzh8"]:
            try:
                br = Browser()
                br.set_handle_robots(False)
                soup = bs4.BeautifulSoup(br.open(url).read(), "html.parser")
                pics = soup.find_all("img")
                pics = [pic["src"] for pic in pics if pic.attrs.has_key("src")]
                [links.append(pic) for pic in pics]
            except Exception as e:
                print("_init_url:", e)
            finally:
                # it frees memory to prevent a memory leak if the html file was a large one
                if soup is not None:
                    soup.decompose()
            print("init urls for input file {} with {} pics".format(url, len(links)))
        return links

    @classmethod
    def get_output_for_url(cls, url):
        """            
            - It maps a url to a downloads path relative to this package
            - ValueError exception in case the url is invalid
        """
        if url is None or not urlparse.urlparse(url).scheme:
            raise exceptions.ValueError("Url is invalid")

        # Retrieves or creates the output dir
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../downloads/")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Appends the target file to the dir
        target_file = urlparse.urlsplit(url).path.split("/")[-1]
        return os.path.join(output_dir, target_file.rstrip())

