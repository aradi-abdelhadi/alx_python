#!/usr/bin/python3
""" Script that takes a URL, sends a request, and displays the response """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        response = requests.get(url)

        print(response.text)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
    else:
        print("Usage: ./4-error_code.py <URL>")
        sys.exit(1)

