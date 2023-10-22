#!/usr/bin/python3
"""
flask app hbnb
"""
from flask import Flask, abort, render_template
from models import storage
from models.state import State

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


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text='is cool'):
    """
    displays python followed by value of text
    replacing any _ with ' '
    default value of text is is cool
    """
    newtext = ''
    for char in text:
        if char != '_':
            newtext = newtext + char
        else:
            newtext = newtext + ' '
    return 'Python ' + newtext


@app.route('/number/<n>', strict_slashes=False)
def integer(n):
    """
    confirms if n is an integer then displays it
    """
    if n.isdigit():
        return '{} is a number'.format(n)
    return abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def displayhtml(n):
    """
    renders a html page if passed value is an integer
    """
    if n.isdigit():
        return render_template('5-number.html', n=n)
    return abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def evenorodd(n):
    """
    renders a html page if passed value is odd or even
    """
    value = ''
    if n.isdigit():
        n = int(n)
        if n % 2 == 0:
            value = '{} is even'.format(n)
        else:
            value = '{} is odd'.format(n)
        return render_template('6-number_odd_or_even.html', value=value)
    return abort(404)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display a HTML page of the States
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(error):
    """
    Closes the database again at the end of the request.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Display a HTML page of the States and the
    Cities by State
    """
    states = storage.all(State).values()
    cities = list()
    for state in states:
        for city in state.cities:
            cities.append(city)
    return render_template('8-cities_by_states.html',
                           states=states, state_cities=cities)


if __name__ == '__main__':
    """
    when run as main app
    runs on localhost and on port 5000
    """
    app.run(host='0.0.0.0', port=5000)
