from optparse import OptionParser

import os
import codecs
import bs4 as bs4
import mechanize as browser


def parse_options():
    parser = OptionParser()
    default_input_file = os.path.join(os.path.abspath("../downloads/"), "input_urls.txt")
    parser.add_option("-i", "--input-file", action="store", dest="input_file", default=default_input_file)
    (options, args) = parser.parse_args()
    if options is not None:
        return unicode(options.input_file)
    return None


class Initializer:
    """
        It parses the arguments of the script.
        In case the --input-file is not found a file is generated.
    """

    def __init__(self):
        self._output_txt = None
        self._is_unit_test = False

    def execute(self, is_unit_test=False):
        """
            It parses the options, fetch htmls and parsers pics inside the htmls
        """
        self._is_unit_test = is_unit_test
        self._output_txt = parse_options()
        # In case the file does not exists it generates a file with urls
        if not os.path.exists(self._output_txt):
            self._init_urls()
        return self.output_txt

    @property
    def output_txt(self):
        return self._output_txt

    def _init_urls(self):
        urls = ["https://goo.gl/W0cMUf",
                    "https://goo.gl/oDi4jg",
                    "https://goo.gl/qBcMct",
                    "https://goo.gl/9MbBMk",
                    "https://goo.gl/Kr0nmT",
                    "https://goo.gl/MDTzh8"]
        for url in urls:
            self._init_url(url)
            if self._is_unit_test:
                break

    def _init_url(self, input_html):
        """
            It parses the html in the input and stores the pictures in the output_txt
        """
        try:
            br = browser.Browser()
            br.set_handle_robots(False)
            response = br.open(input_html)
            response_txt = response.read()
            count = 0
            soup = bs4.BeautifulSoup(response_txt, "html.parser")

            pics = soup.find_all("img")
            pics = (pic["src"] for pic in pics if pic.attrs.has_key("src"))
            with codecs.open(self.output_txt, "w", "utf-8") as f:
                for pic in pics:
                    f.write("{}\n".format(pic))
                    count += 1
        except Exception as e:
            print "_init_url:", e
        finally:
            # it frees memory, specially important if the html file was a large one
            if soup is not None:
                soup.decompose()
        print("init urls for input file {} with {} pics".format(input_html, count))