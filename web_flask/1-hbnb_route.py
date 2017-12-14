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

app.run(host='0.0.0.0')
