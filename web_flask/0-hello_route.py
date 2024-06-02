#!/usr/bin/python3
from flask import Flask
"""
a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
    You must use the option strict_slashes=False in your route
    definition
"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displaying Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
