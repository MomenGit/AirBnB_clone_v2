#!/usr/bin/python3
"""A Flask web app that has routes '/' & '/hbnb'"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Returns “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Returns “C ” followed by text"""
    return "C {}".format(text.replace('_', ' '))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Returns “Python ” followed by text"""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Returns “n is a number”"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Returns “n is a number”"""
    return render_template('5-number.html', n=n).upper()


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Return template with Number: n is even|odd"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
