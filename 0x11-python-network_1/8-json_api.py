#!/usr/bin/python3
"""this script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter"""


import requests
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        r = requests.post('http://0.0.0.0:5000/search_user', q=argv[1])
    else:
        r = requests.post('http://0.0.0.0:5000/search_user', q="")
        print('No result')
    response_bodytype = r.headers.get('Content-Type')
    if response_bodytype == 'application/json':
        json_content = eval(r.content)
        if json_content != {}:
            print('[{}] {}'.format(json_content['id'], json_content['name']))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
