#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, escape

app = Flask(__name__)

# Route to display "Hello HBNB!" on the root URL ("/")
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

# Route to display "HBNB" on the "/hbnb" URL
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

# Route to display "C " followed by the value of the text variable
# Replace underscore _ symbols with a space
@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    return 'C {}'.format(escape(text.replace('_', ' ')))

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)
:
