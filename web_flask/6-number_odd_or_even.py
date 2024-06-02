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
        /number_template/<n>: display a HTML page only if n is an integer:
                        - H1 tag: “Number: n” inside the tag BODY
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
                        - H1 tag: “Number: n is even|odd” inside the tag BODY
    You must use the option strict_slashes=False in your route definition
"""
from flask import Flask
from flask import render_template


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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Renders an HTML page displaying the number passed in the URL path.
    The page includes an H1 tag with the text "Number: n".

    Args:
        n (int): The integer number to be displayed on the HTML page.

    Returns:
        str: The rendered HTML content.
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    Renders an HTML page displaying the number passed in the URL path and
    indicates whether the number is even or odd.

    Args:
        n (int): The integer number to be checked for evenness or oddness.

    Returns:
        str: The rendered HTML content indicating whether the number is even
        or odd.
    """
    if n % 2 == 0:
        odd_even = 'even'
    else:
        odd_even = 'odd'
    # Render an HTML template with the number and whether it is odd or even
    return render_template('6-number_odd_or_even.html', number=n,
            odd_even=odd_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
