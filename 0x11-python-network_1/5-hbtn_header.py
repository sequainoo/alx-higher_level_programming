#!/usr/bin/python3
'''sends a request to url and displays value of the X-Request-Id header.'''
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    res = requests.get(url)
    x_request_id = res.headers.get('X-Request-Id')
    print(x_request_id)

    
