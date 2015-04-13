#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import logging

def get_app():
    app = Flask(__name__)
    app.config.from_object(__name__ + '.config')

    app.logger.setLevel(logging.DEBUG)
    return app

