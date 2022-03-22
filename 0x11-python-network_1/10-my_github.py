#!/usr/bin/python3
'''
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''
import sys
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    pat = sys.argv[2]
    res = requests.get(url, auth=(username, pat))
    if res.status_code >= 400:
        print(None)
    else:
        j_data = res.json()
        print(j_data['id'])
