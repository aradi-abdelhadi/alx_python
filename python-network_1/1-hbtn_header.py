#!/usr/bin/python3
""" Script that takes a URL, sends a request, and displays the value of X-Request-Id """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
    else:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

