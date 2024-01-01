"""script that starts a Flask web application

web application must be listening on 0.0.0.0
port 5000
Routes:
        /c/<text>:  display “C ” followed by the
        value of the text variable
"""


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
  """displays “Hello HBNB!”"""
  return "Hello world"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
  """displays “Hello HBNB!”"""
  return "Hello HBNB!"

@app.route("/c/<text>", strict_slashes=False)
def hbnb():
  """display “C ” followed by the
  value of the text variable"""
  text = text.replace("_", " ")
  return f'C {text}'

if __name__ == "__main__":
  app.run(host="0.0.0.0")