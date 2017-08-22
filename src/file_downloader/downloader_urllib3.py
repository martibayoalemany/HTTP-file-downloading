""" Download with urllib3 """
# pylint: skip-file

import urllib3

if False : 
    verbose = False
    serialize = False

    from hyper import HTTPConnection
    from mechanize import Request, urlopen
    from constants import Constants

    import exceptions
    import multiprocessing
    import time
    import traceback
    import six
    import urlparse


    def download_parallel(links, num_processes=1):
        """ Downloads the list of :links: """
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


    
    def download(url):
        """
            TO-DO - finish hyper api connection
            c = HTTPConnection(graphai.facebook.FACEBOOK_GRAPH_URL)
            stream_id = c.request('GET', graph.get_me_query_path())
            resp = c.get_response()
            print resp.headers
            print resp.status
            print resp.read()

           # Using requests and hyper
            s = requests.Session()
            s.mount(graphai.facebook.FACEBOOK_GRAPH_URL, HTTP20Adapter())
            r = s.get(graph.get_me_query_path())
            r2 = s.get(graph.get_me_query_path())
        """
        try:
            if url is None or not isinstance(url, six.types.StringTypes):
                return False, "No url was given to download"
            if verbose:
                print(
                    "[Process: {}] - Downloading url {} ".format(multiprocessing.current_process(), url))

            url_p = urlparse.urlparse(url)
            conn = HTTPConnection(url_p.hostname)
            conn.request('GET', '{}?{}'.format(url_p.path, url_p.query))
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
