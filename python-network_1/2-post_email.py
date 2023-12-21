#!/usr/bin/python3
""" Script that takes a URL and an email address, sends a POST request, and displays the response """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        payload = {'email': email}
        response = requests.post(url, data=payload)
        print("Your email is:", email)
        print(response.text)
    else:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

