"""
  Download with hyper
"""
import exceptions
import multiprocessing
import time

from .constants import Constants

verbose = False
serialize = False


def download_parallel(links, max_links=-1, num_processes=1):
    """
      Download files with hyper in parallel
    """
    if isinstance(links, list) and len(links) is 0:
        links = Constants.load_links(max_links)
    start = time.time()

    pool = multiprocessing.Pool(processes=num_processes)

    results = pool.map(download, links)
    pool.close()
    pool.join()

    failed = [r[0] for r in results if not r[0]]

    print("Download with {} processes and {} links took {}, failed {} "
          .format(num_processes, len(links), (time.time() - start), len(failed)))

    if any(len(failed)):
        raise exceptions.OSError("Failed {}".format(len(failed)))


def download(url):
    # TODO: implement downloading with hyper
    raise exceptions.NotImplementedError
    """
    try:
        if url is None or not isinstance(url, six.types.StringTypes):
            return False, "No url was given to download"
        if verbose:
            print("[Process: {}] - Downloading url {} ".format(multiprocessing.current_process(), url))

        url_p = urlparse.urlparse(url)
        target = "{}://{}?{}".format(url_p.scheme, url_p.hostname, url_p.query)
        conn = HTTPConnection(target)
        conn.request('GET', url_p.path)
        resp = conn.get_response()

        if Constants.picture_serialization:
            with open(Constants.get_output_for_url(url), "wb") as f:
                f.write(resp.read())
        else:
            # For performance measurement
            resp.read()
        return True,
    except Exception as e:
        return False,
    """
