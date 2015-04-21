#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.sqlalchemy import SQLAlchemy
from flask_json import app

db = SQLAlchemy(app)
