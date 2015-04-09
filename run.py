#! /usr/bin/env python
# -*- coding: utf-8 -*-

import flask
from flask import jsonify
from flask_json import app, db

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
    conn = db.connect()
    result = conn.execute("select * from user")

    return jsonify(result.first())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
