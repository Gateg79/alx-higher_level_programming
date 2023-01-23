#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)
"""

from urllib import request
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
