#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from flask.ext.sqlalchemy import SQLAlchemy

from flask_json import app

def get_local_db_conf():
    path = os.path.dirname(os.path.abspath(__file__))
    local_dbauth_path = os.path.join(path, 'dbauth')
    if not os.path.exists(local_dbauth_path):
        return
    with open(os.path.join(path, 'dbauth')) as f:
        return f.readline().rstrip().split(':')

def get_database(app):
    PUBLIC_MYSQL_URI = 'mysql+pymysql://{}:{}@localhost/flask_json?charset=utf8'
    DATABASE = PUBLIC_MYSQL_URI.format(*get_local_db_conf())
    engine = create_engine(DATABASE, pool_recycle=3600)
    return engine

db = SQLAlchemy(app)
