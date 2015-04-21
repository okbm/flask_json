#! /usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from flask import jsonify
import flask_json
from flask_json import app, database
from flask_json.models.User import *

@app.route('/')
def top():
    """html"""
    return flask.render_template('index.html')

@app.route('/json')
def sample_json():
    """json"""
    users = {'1':'john', '2':'steve', '3':'bill'}
    return jsonify(users)

@app.route('/sql')
def sample_sql():
    """json + mysql"""
    users = User.query.all()

    result = {}
    for user in users:
        result[user.id] = user.name

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
