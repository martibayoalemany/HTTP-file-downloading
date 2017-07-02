"""
  It downloads pictures using multiprocessing.Pool and the Request api

"""
# pylint: skip-file
from mechanize import Request, urlopen
from constants import Constants

import multiprocessing
import time
import traceback
import exceptions
import six

verbose = False


def download_dummies(max_links=-1, num_processes=1):
    """
      It download some constant dummy files
    """
    if len(links) is 0:
        links = Constants.load_links(max_links)
    download_parallel(links, num_processes)


def download_parallel(links, num_processes=1):
    """
      Downloads the list of :links:
    """
    start = time.time()
    pool = multiprocessing.Pool(processes=num_processes)

    results = pool.map(download, links)

    pool.close()
    pool.join()

    failed = [r[0] for r in results if not r[0]]

    print("Download with {} processes and {} links in {}, failed {} "
          .format(num_processes, len(links), (time.time() - start), len(failed)))

    if len(failed) == num_processes:
        raise exceptions.OSError("Failed {}".format(len(failed)))


def download(url, serialize=Constants.picture_serialization):
    """
        Download the given url and serialize depending on the parameter
    """
    try:
        if url is None or not isinstance(url, six.types.StringTypes):
            print("No url was given to download")
            return (False, "No url was given to download", url)
        target = Constants.get_output_for_url(url)
        if verbose:
            print(u"[Process: {}] - Downl. url {} - {}"
                  .format(multiprocessing.current_process(), url, target))
        req = Request(url)
        web_file = urlopen(req)
        if serialize:
            with open(target, "wb") as handle:
                handle.write(web_file.read())
        else:
            # For performance measurements
            web_file.read()
        return (True, None, url)
    except Exception as e:
        print(e)
        return (False, e, url)


def main():
    print("Downloader main method")


if __name__ == "__main__":
    print("Main method of file ", __file__)
