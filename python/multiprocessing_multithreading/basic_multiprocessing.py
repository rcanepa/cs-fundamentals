import urllib.request
from multiprocessing.pool import ThreadPool
import random
import time

sites = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://www.macrumors.com/',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
]


def url_size(url):
    time.sleep(random.random() + 5)
    with urllib.request.urlopen(url) as u:
        page = u.read()
        return url, len(page)


pool = ThreadPool(10)
for result in pool.imap_unordered(url_size, sites):
    print(result)
