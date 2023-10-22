#!/usr/bin/python3
"""
Defines /states_list: that displays an HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage sorted by name (A->Z) tip
    LI tag: description of one State: <state.id>: <B><state.name></B>
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def states_list():
    """Returns an HTML page containing list of states"""
    states_list = storage.all(State).values()
    return render_template("7-states_list.html", states=states_list)


@app.teardown_appcontext
def close_db_session(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
