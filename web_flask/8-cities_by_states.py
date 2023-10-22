#!/usr/bin/python3
"""Docs"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Returns an HTML page containing list of states"""
    states_list = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states_list)


@app.teardown_appcontext
def close_db_session(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
