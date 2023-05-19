#!/usr/bin/python3
"""this script takes my GitHub credentials (username and password) and
uses the GitHub API to display my id
I used Basic Authentication with a personal access token as password
to access to my information (only read:user permission is needed)
The first argument will be my username
The second argument will be my personal access token as password"""


from requests.auth import HTTPBasicAuth
import requests
from sys import argv

if __name__ == "__main__":
    basic = HTTPBasicAuth(argv[1], argv[2])
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get('id'))
