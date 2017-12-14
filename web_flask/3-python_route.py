#!/usr/bin/python3
"""helloBNBN"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return ("Hello HBNB!")

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return ("HBNB")

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return ("C {}".format(text.replace("_", " "))

@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    return ("Python {}".format(text.replace("_", " "))


app.run(host='0.0.0.0')
