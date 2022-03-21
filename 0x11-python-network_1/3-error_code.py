#!/usr/bin/python3
'''Sends a a request to url handles HTTPError and displays response body
'''
import sys
from urllib import error, request

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            data = response.read()
            data = data.decode('utf-8')
            print(data)
    except error.HTTPError as e:
        print('Error code: {}'.format(e.status))
