#!/usr/bin/python3
"""
flask app hbnb
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    when visit home route returns a sting
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns a string when you visit the route
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """
    displays C followed by the value of text variable
    """
    newtext = ''
    for char in text:
        if char != '_':
            newtext = newtext + char
        else:
            newtext = newtext + ' '
    return 'C ' + newtext


if __name__ == '__main__':
    """
    when run as main app
    runs on localhost and on port 5000
    """
    app.run(host='0.0.0.0', port=5000)
