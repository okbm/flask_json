#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask_json.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    created = db.Column(db.DateTime)
    def __init__(self, id, name, created):
        self.id = id
        self.name = name
        self.created = created

