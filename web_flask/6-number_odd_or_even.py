#!/usr/bin/python3
"""helloBNBN"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """docs"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """docs"""
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """docs"""
    return ("C {}".format(text.replace("_", " ")))

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """docs"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """docs"""
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_template_n(n):
    """docs"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_even(n):
    """docs"""
    if n % 2:
        msg = "{} is odd".format(n)
    else:
        msg = "{} is even".format(n)
    return render_template('6-number_odd_or_even.html', msg=msg)

app.run(host='0.0.0.0', port=5000)
