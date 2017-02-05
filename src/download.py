import os
from optparse import OptionParser

import bs4 as bs4
import mechanize as mechanize



def parse_options():
    parser = OptionParser()
    parser.add_option("-i", "--input-urls", action="store", dest="input_urls", default = None)
    (options, args) = parser.parse_args()
    return options.input_urls

if __name__ == '__main__':

    print(" ---> {} --- {} --- {} " % os.path.abspath("downloads"), os.path.dirname(__file__), os.path.curdir)
    # input_file = parse_options()

    default_url = "https://goo.gl/vMRehT"
    br = mechanize.Browser()
    br.set_handle_robots(False)
    response = br.open(default_url)
    response_txt = response.read()
    try:
        soup = bs4.BeautifulSoup(response_txt, "html.parser")
        soup.find_all("div", attrs="data")
    finally:
        if soup is not None:
            soup.decompose()

