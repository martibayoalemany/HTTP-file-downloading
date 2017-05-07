import itertools
import multiprocessing
import time
import six
from mechanize import Request, urlopen
from constants import Constants


class Downloader:
    verbose = False

    def __init__(self):
        pass

    def execute(self, num_processes=1):
        links = Constants.load_links()
        start = time.time()
        chunks = itertools.tee(links, num_processes)
        processes = list()
        for chunk in chunks:
            p = multiprocessing.Process(target=lambda chunk_param: [self._doExecute(url) for url in chunk_param],
                                        args={chunk})
            processes.append(p)
        [p.start() for p in processes]
        [p.join() for p in processes]
        print("Download with {} processes and {} links took {}".format(processes, len(links), (time.time() - start)))

    @classmethod
    def _doExecute(cls, url):
        try:
            if url is None or not isinstance(url, six.types.StringTypes):
                raise ValueError("No url was given to download")
            if cls.verbose:
                print("[Process: {}] - Downloading url {} ".format(multiprocessing.current_process(), url))
            req = Request(url)
            web_file = urlopen(req)
            with open(Constants.get_output_for_url(url), "wb") as f:
                f.write(web_file.read())
        except Exception as e:
            raise e

if __name__ == '__main__':
    Downloader().execute(num_processes=2)
    Downloader().execute(num_processes=6)
