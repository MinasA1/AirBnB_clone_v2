#!/usr/bin/python3
"""helloBNBN"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return ("Hello HBNB!")

app.run(host='0.0.0.0')

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return ("HBNB")

app.run(host='0.0.0.0')
