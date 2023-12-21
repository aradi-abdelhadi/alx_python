import requests
import sys

url = sys.argv[1]  # Get the URL from the first command-line argument
email = sys.argv[2]  # Get the email from the second command-line argument

response = requests.post(url, data={"email": email})

print(response.text)  # Print the body of the response

