#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging

app = Flask(__name__)
app.config.from_object(__name__ + '.settings')

import flask_json.database
