#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask, render_template

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
    return 'C {}'.format(text.replace('_', ' '))

# Route to display "Python " followed by the value of the text variable
# Replace underscore _ symbols with a space
# Default value for text is "is cool"
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_is_cool(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))

# Route to display a HTML page only if n is an integer
# H1 tag: “Number: n” inside the tag BODY
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0:5000
    app.run(host='0.0.0.0', port=5000)

