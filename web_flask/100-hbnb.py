#!/usr/bin/python3
"""Docs"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns an HTML page containing list of states"""
    data = {
        "states": storage.all(State).values(),
        "amenities": storage.all(Amenity).values(),
        "places": storage.all(Place).values(),
        "users": storage.all(User).values()
    }

    return render_template("100-hbnb.html", models=data)


@app.teardown_appcontext
def close_db_session(error):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
