#!/usr/bin/python3
"""script that starts a Flask web application

web application must be listening on 0.0.0.0
port 5000
Routes:
        /number_template/<n>: display a HTML
        page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
"""


from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays “Hello HBNB!”"""
    return "HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Displays “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f'C {text}'


@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Displays “Python ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f'Python {text}'


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """Displays “n is a number” only if n is an integer"""
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)