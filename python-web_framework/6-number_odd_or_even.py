from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    Route for the root endpoint.

    Returns:
        str: Greeting message.
    """
    return "Hello HBNB!"

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Route to determine if a number is odd or even.

    Args:
        n (int): The input number.

    Returns:
        str: HTML template rendering the number and its parity.
    """
    # Check if the number is even or odd
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    
    # Render the template with the number and its parity
    return render_template('6-number_odd_or_even.html', number=n, parity=parity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

