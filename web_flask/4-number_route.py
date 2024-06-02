#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ” followed by the value of the text
                   variable (replace underscore _ symbols with a space )
        /python/<text>: display “Python ”, followed by the value of the
                        text variable (replace underscore _ symbols with
                        a space )
                        - The default value of text is “is cool”
        /number/<n>: display “n is a number” only if n is an integer
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays "Hello HBNB!" when the root URL ("/") is accessed.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" when the "/hbnb" URL is accessed.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Replaces underscores with spaces in the given text and displays "C
    <modified_text>".

    Args:
        text (str): The input text with underscores that need to be replaced
        with spaces.

    Returns:
        str: A string formatted as "C <modified_text>", where underscores in
        the original text have been replaced with spaces.
    """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is cool'):
    """
    Replaces underscores with spaces in the given text and displays "Python
    <modified_text>".

    Args:
        text (str): The input text with underscores that need to be replaced
        with spaces.

    Returns:
        str: A string formatted as "Python <modified_text>", where underscores
        in the original text have been replaced with spaces.
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Displays the input number followed by " is a number".

    Args:
        n (int): The integer number to be displayed.

    Returns:
        str: A string formatted as "<number> is a number".
    """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
