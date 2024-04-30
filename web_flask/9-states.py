#!/usr/bin/python3
"""
A script that starts a Flask web application to load all cities of a State.

If the storage engine is DBStorage use cities relationship otherwise use the
public getter method cities relationship.

After each request remove the current SQLAlchemy session declare a method
to handle @app.teardown_appcontext and call storage.close() method

GET /states
GET /states/<id>
    displays a HTML page according to templates/9-states.html
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(_):
    """Close DB session"""
    storage.close()



@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """GET /states and /states/<id>"""
    states = storage.all(State, id)
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
