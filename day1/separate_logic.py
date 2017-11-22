from functools import wraps
import time
import requests


def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = requests.get(url).text
    saved[url] = page
    return page


def cache(func):
    saved = {}
    @wraps(func)
    def cacher(arg):
        if arg in saved:
            return saved[arg]
        result = func(arg)
        saved[arg] = result
        return result
    return cacher


@cache
def web_lookup2(url):
    return requests.get(url).text

def main():
    start = time.time()
    r1 = web_lookup2("http://cnn.com")
    print("It took", time.time()-start , "seconds")
    start = time.time()
    r2 = web_lookup2("http://cnn.com")
    print("It took", time.time()-start , "seconds")
    print(r1 == r2)


if __name__ == '__main__':
    main()