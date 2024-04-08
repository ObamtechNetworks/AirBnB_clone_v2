#!/usr/bin/python3
""" Module that sets up flask application """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def display_states_list():
    """ Displays a list of states """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current sqlalchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
