#!/usr/bin/python3
"""this script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8). It manages
urllib.error.HTTPError exceptions and prints: Error code: followed
by the HTTP status code"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
