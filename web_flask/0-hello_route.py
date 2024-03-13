#!/usr/bin/python3
# A script that starts flask
""" module doc """
from flask import Flask

app = Flask(__name__)


@app.route("/airbnb-onepage/", strict_slashes=False)
def hello():
    """ dispalay hello HBNB"""
    return "Hello HBNB!"


if __name__ == "__main__":
    """Start flask development server"""
    app.run(host="0.0.0.0", port=5000)
