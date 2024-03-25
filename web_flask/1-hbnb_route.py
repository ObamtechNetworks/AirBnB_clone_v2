#!/usr/bin/python3
"""
A script that starts a flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    Must use the option- strict_slashes=False
"""

# import modules
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns hello hbnb!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns 'hbnb'"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
