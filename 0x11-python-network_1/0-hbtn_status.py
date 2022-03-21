#!/usr/bin/python3
'''Fetches https://alx-intranet.hbtn.io/status

prints:
    the type of the response.
    content of response as is or as bytes
    and decoded content of response with utf-8

only urllib
'''
from urllib import request

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'
    try:
        with request.urlopen(url) as response:
            content = response.read()
            print('Body response:')
            print('\t- type: {}'.format(type(content)))
            print('\t- content: {}'.format(content))
            print('\t- utf8 content: {}'.format(content.decode('utf-8')))
    except BaseException as e:
        pass
