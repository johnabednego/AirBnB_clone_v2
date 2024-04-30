#!/usr/bin/python3
"""
A script that stars a Flask web application to load all cities
of a State.
If the storage engine is DBStorage, you must use cities relationship
otherwise use the public getter method cities. After each session
declare a method to handle @app.teardown_appcontext and call the
storage.close() method.

Get /cities_by_states
    displays a HTML page of the structure in templates/8-cities_by_states.html
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(_):
    """close session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display cities by states"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
