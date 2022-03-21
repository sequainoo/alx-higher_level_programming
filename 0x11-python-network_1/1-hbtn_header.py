#!/usr/bin/python3
'''Sends http request to the url and returns value of X-Request-Id header.'''
import sys
from urllib import request
from urllib.error import HTTPError, URLError

if __name__ == '__main__':
    url = sys.argv[1]
    print(url)
    try:
        with request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            print(x_request_id)
    except HTTPError as e:
        pass
    except URLError as e:
        pass
