import logging.config, json, os
from flask import request

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

log_path = os.path.join(__location__, "site.log")

def init_app(app):
        
    logging.config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": { 
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            },
            "json": { 
                "format": '{"date-time": "%(asctime)s", "line": "%(lineno)d", "function": "%(funcName)s", "module": "%(module)s", "level_name": "%(levelname)s", "messages": "%(message)s"},'
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
                },
            "file": {
                "class": "logging.FileHandler",
                "filename": "website\\utility\\site.log",
                "formatter": "json",
                "level": "DEBUG",
                },
            "size-rotate": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "website\\utility\\site.log",
                "maxBytes": 1000000,
                "backupCount": 5,
                "formatter": "json",
                "level": "DEBUG"
                },
        },
        "loggers": {
            "console": {"level": "DEBUG", "handlers": ["console"]},
            "file": {"level": "DEBUG", "handlers": ["file"]},
            },
        "root": {
            "level": "DEBUG" ,"handlers": ["console", "file"] 
        }
    })