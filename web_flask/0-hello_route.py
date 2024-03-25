#!/usr/bin/python3
"""
A scrip that starts a flask web application
Web application must be listening on 0.0.0.0, port 5000
Routes
    /: display "Hello HBNB!"
    Must use the option- strict_slashes=False
"""

# import modules
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_hbnb():
    """returns hello hbnb!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
