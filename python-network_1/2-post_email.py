#!/usr/bin/python3
""" Script that takes in a URL and an email address, sends a POST request, and displays the response """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        
        # Ensure the correct URL formatting by adding '?' if needed
        separator = '&' if '?' in url else '?'
        url = f'{url}{separator}email={email}'
        
        response = requests.post(url)
        print("Your email is:", email)
        print(response.text)
    else:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

