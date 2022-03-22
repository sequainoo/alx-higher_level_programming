#!/usr/bin/python3
'''script sends post request sending a character as parameter.
'''
import sys
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) < 2:
        parameter = ''
    else:
        parameter = sys.argv[1]
    payload = {'q': parameter}
    res = requests.post(url, data=payload)
    if res.content:
        try:
            j_data = res.json()
            if j_data:
                print('[{}] {}'.format(j_data.get('id'), j_data.get('name')))
            else:
                print('No result')
        except BaseException as e:
            print('Not a valid JSON')
