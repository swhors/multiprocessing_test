import functools

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

from app.config import Config
import os

_flask_db: SQLAlchemy
_flask_app: Flask


def get_flask() -> ():
    global _flask_app, _flask_db
    print(f'get_flask-{os.getpid()}/{os.getppid()} = {_flask_db}, {_flask_app}')
    if _flask_app is None:
        print(f'flask_app is None. [{_flask_app}/{_flask_db}]')
        init_flask()
    return _flask_app, _flask_db


def init_flask(config: Config = None) -> Flask:
    global _flask_app, _flask_db
    if config is None:
        from app.config import current_config
        config = current_config
    _flask_app = Flask("multiprocessing")
    _flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.mysql.db_url
    _flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    _flask_app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600
    _flask_app.secret_key = 'manyrandombyte'
    _flask_db = SQLAlchemy(_flask_app)
    # from models import info, user
    # db.create_all()

    return _flask_app


def enter_flask_sqlalchemy(func):
    def inner(*args, **kwargs):
        _flask_app.app_context().push()
        ret_val = func(*args, **kwargs)
        _flask_db.session.commit()
        return ret_val
    return inner


def enter_flask_sqlalchemy_no_commit(func):
    def inner(*args, **kwargs):
        _flask_app.app_context().push()
        ret_val = func(*args, **kwargs)
        return ret_val
    return inner
