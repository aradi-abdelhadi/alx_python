#!/usr/bin/python3
""" Script that takes a letter, sends a POST request, and displays the response """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': letter}

    try:
        response = requests.post(url, data=payload)
        json_data = response.json()

        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

