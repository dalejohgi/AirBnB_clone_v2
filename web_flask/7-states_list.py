#!/usr/bin/python3
"""Module"""

from flask import Flask
from flask import render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(self):
	"""refresh the session"""
	storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
	"""Displays the states list"""
	states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
	return render_template('7-states_list.html', states=states)
if __name__ == '__main__':
	app.run(host='0.0.0.0', port='5000', debug=True)

