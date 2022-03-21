#!/usr/bin/python3
'''Sends http request to the url and returns value of X-Request-Id header.'''
import sys
from urllib import request


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            print(x_request_id)
    except BaseException as e:
        pass
