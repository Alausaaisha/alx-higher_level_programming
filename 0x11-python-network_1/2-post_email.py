#!/usr/bin/python3
"""this script takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)"""

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    post_dict = {'email': argv[2]}
    url_encoded_data = urlencode(post_dict)
    post_data = url_encoded_data.encode("utf-8")
    with urlopen(Request(argv[1], data=post_data)) as response:
        body = response.read()
        print(body.decode("utf-8"))
