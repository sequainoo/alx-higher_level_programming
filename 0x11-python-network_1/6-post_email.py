#!/usr/bin/python3
'''Using requests to send post request.'''
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    payload = dict(email=email)
    res = requests.post(url, data=payload)
    print(res.text)
