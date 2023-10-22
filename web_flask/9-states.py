#!/usr/bin/python3
"""
Defines /states: that displays an HTML page: (inside the tag BODY)
and Defines /states/<id>: that displays a HTML page: (inside the tag BODY)
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Returns an HTML page containing list of states"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def state(id):
    """Returns an HTML page containing a state with its cities"""
    state = storage.all(State).get("State.{}".format(id))
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def close_db_session(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
