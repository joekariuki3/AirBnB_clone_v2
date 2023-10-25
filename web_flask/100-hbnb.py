#!/usr/bin/python3
"""
flask app hbnb
"""
from models.amenity import Amenity
from flask import Flask, abort, render_template
from models.place import Place
from models import storage
from models.state import State
from models.user import User

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    when visit home route returns a sting
    """
    return 'Hello HBNB!'


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


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=0):
    """
    display a specific state acording to the
    passed id
    """
    states = storage.all(State).values()
    if id == 0:
        return render_template('9-states.html', states=states)
    state_name = ''
    cities = list()
    for state in states:
        if state.id == id:
            state_name = state.name
            for city in state.cities:
                cities.append(city)
    return render_template('9-states.html',
                           state_name=state_name, cities=cities)


@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """
    returns the filterd data at the search bar from the db
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    returns all the data to the html from
    the database
    """
    states = storage.all(State).values()
    places = storage.all(Place).values()
    amenities = storage.all(Amenity).values()
    users = storage.all(User).values()
    return render_template('100-hbnb.html', states=states,
                           places=places, amenities=amenities, users=users)


@app.teardown_appcontext
def teardown_db(error):
    """
    Closes the database again at the end of the request.
    """
    storage.close()


if __name__ == '__main__':
    """
    when run as main app
    runs on localhost and on port 5000
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
