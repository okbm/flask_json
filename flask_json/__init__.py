#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_json.models import database
import logging

app = Flask(__name__)
app.config.from_object(__name__ + '.config')

app.logger.setLevel(logging.DEBUG)

#db = SQLAlchemy(app)
db = database.get_database(app)

