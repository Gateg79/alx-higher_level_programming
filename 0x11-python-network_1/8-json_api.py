#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        res = r.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res['id'], res['name']))
    except Exception:
        print("Not a valid JSON")
