#!/usr/bin/python3
"""helloBNBN"""
from flask import Flask
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


@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """docs"""
    return ("Python {}".format(text.replace("_", " ")))


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """docs"""
    return ("{} is a number".format(n))


app.run(host='0.0.0.0')
