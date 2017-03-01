import os
import codecs

from downloader import Downloader
from initializer import Initializer

if __name__ == '__main__':

    initializer = Initializer()
    input_txt = initializer.execute()

    # It downloads the pics with regular http1.1
    if os.path.exists(input_txt):
        with codecs.open(input_txt, "r", "utf-8") as f:
            urls = [line for line in f]
            d = Downloader()
            d.download(urls)