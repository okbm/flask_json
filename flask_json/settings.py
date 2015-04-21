#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
from sqlalchemy import create_engine

def get_local_db_conf():
    path = os.path.dirname(os.path.abspath(__file__))
    local_dbauth_path = os.path.join(path, 'dbauth')
    if not os.path.exists(local_dbauth_path):
        return
    with open(os.path.join(path, 'dbauth')) as f:
        return f.readline().rstrip().split(':')

def get_database_url():
    PUBLIC_MYSQL_URI = 'mysql+pymysql://{}:{}@localhost/flask_json?charset=utf8'
    return PUBLIC_MYSQL_URI.format(*get_local_db_conf())

def get_database_engine():
    PUBLIC_MYSQL_URI = 'mysql+pymysql://{}:{}@localhost/flask_json?charset=utf8'
    DATABASE = PUBLIC_MYSQL_URI.format(*get_local_db_conf())
    engine = create_engine(DATABASE, pool_recycle=3600)
    return engine

DEBUG = True
SQLALCHEMY_DATABASE_URI = get_database_url()
