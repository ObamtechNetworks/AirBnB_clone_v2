#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays a HTML page listing all State objects"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Displays a HTML page listing all cities of a State"""
    state = None
    for obj in storage.all(State).values():
        if obj.id == id:
            state = obj
            break

    if state:
        if storage.__class__.__name__ == "DBStorage":
            cities = [city for city in state.cities]
        else:
            cities = state.cities()
        cities_sorted = sorted(cities, key=lambda city: city.name)
        return render_template('9-states.html',
                               state=state,
                               cities=cities_sorted)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
