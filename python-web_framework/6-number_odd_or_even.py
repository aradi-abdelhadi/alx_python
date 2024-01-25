from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    return render_template('6-number_odd_or_even.html', number=n, parity=parity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

