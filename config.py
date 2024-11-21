"""Flask config."""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))

class Config(object):
    DEBUG = True
    TESTING = False
    FLASK_ENV = 'development'
