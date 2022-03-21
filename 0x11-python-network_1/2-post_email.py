#!/usr/bin/python3
'''Script sends a post request with email as parameter.

Accepts url and email as args.
'''
import sys
from urllib import request, error, parse

if __name__ == '__main__':
    url = sys.argv[1]
    data = {'email': sys.argv[2]}
    data = parse.urlencode(data)
    data = data.encode('ascii')
    req = request.Request(url, data)
    try:
        with request.urlopen(req) as response:
            content = response.read()
            print(content.decode('utf-8'))
    except error.HTTPError as e:
        pass
    except error.URLError as e:
        pass
