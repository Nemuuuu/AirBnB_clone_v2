#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
# import 7-dump.sql

app = Flask(__name__)
app.strict_slashes = False

@app.teardown_appcontext
def close_DB(self):
    """ remove current session """
    storage.close()

@app.routes('/states_list')
def state_lists():
    """ displays all lists present in DB storage"""
    return render_template('7-states_list.html',
                           state=storage.all(State).values())

@app.route('/cities_by_states')
def cities_by_states():
    """
    Displays all cities in a state present in DBStorage
    """
    return render_template('8-cities_by_states.html',
                           state=storage.all(State).values())
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

