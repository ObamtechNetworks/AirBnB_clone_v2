#!/usr/bin/python3
"""
A script that starts a flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes
    /: display "Hello HBNB!"
    /hbnb: display "HBNB"
    /c/<text>: display "C" follwed by the value of the text
    variable (replaces underscores with space
    Must use the option- strict_slashes=False
    /python/<text>: dipslay "Python" followed by the value of text
        the deafult value of text is "is cool"
"""

# import modules
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """returns hello hbnb!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """returns 'hbnb'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_C_with_texts(text):
    """display 'C' followed by the value of the text variable"""
    # if "_" in text:
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_text(text):
    """returns python is <given text string>"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
