#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
import os

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays list of states, city and amenities"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)

    cities = []
    # Fetch ctieis using relationshiop or public getter method
    if os.getenv('HBNB_STORAGE_TYPE') == 'db':
        for state in sorted_states:
            cities.extend(state.cities)
    else:
        for state in sorted_states:
            cities.extend(state.cities)

    amenities = storage.all(Amenity).values()
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=sorted_states,
                           cities=cities,
                           amenities=sorted_amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
