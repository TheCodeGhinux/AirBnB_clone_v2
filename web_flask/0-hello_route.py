#!/usr/bin/python3
"""script that starts a Flask web application

web application must be listening on 0.0.0.0
port 5000
Routes: 
        / : Displays Hello world 
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
  """displays “Hello HBNB!”"""
  return "Hello world"

if __name__ == "__main__":
  app.run(host="0.0.0.0")