import logging.config, json, os
from flask import request

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

path = os.path.join(__location__, "site.log")

def init_app(app):
    
    with app.app_context():
        
        logging.config.dictConfig(
        {"version": 1,
        "formatters": {
            "default": { "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
            },
            "json": {
                "format": json.dumps([
                    {"date-time": "%(asctime)s"},
                    {"line": "%(lineno)d"},
                    {"function": "%(funcName)s"},
                    {"module": "%(module)s"},
                    {"level_name": "%(levelname)s"},
                    {"messages": "%(message)s"}])}
            },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
                },
            "file": {
                "class": "logging.FileHandler",
                "filename": "site.log",
                "formatter": "json",
                },
            "size-rotate": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "site.log",
                "maxBytes": 1000000,
                "backupCount": 5,
                "formatter": "json",
                "level": "DEBUG"
                },
            },
        "loggers": {
            "root": {"level": "INFO", "handlers": ["console", "size-rotate"]}
            }
        })