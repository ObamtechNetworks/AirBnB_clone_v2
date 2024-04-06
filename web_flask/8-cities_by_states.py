#!/usr/bin/python3
"""Module that sets up flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities_by_state():
    """Displays a list of cities bystates"""
    states = storage.all("State").values()
    cities = storage.all("City").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template(
            "8-cities_by_states.html",
            states=sorted_states,
            cities=sorted(cities, key=lambda x: x.name))


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current sqlalchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
