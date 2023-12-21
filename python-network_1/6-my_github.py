#!/usr/bin/python3
""" Script that takes GitHub credentials and displays the GitHub id """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 3:
        username = sys.argv[1]
        password = sys.argv[2]

        url = "https://api.github.com/user"
        response = requests.get(url, auth=(username, password))

        try:
            json_data = response.json()
            print(json_data.get('id'))
        except ValueError:
            print("None")
    else:
        print("Usage: ./6-my_github.py <username> <personal_access_token>")
        sys.exit(1)

