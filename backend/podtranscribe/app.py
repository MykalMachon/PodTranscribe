# standard lib imports
import logging
from os import getenv

# third party imports
from flask import Flask
from celery import Celery


def create_flask():
    app = Flask(__name__)
    app.logger.setLevel(logging.INFO)

    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    @app.get('/')
    def get_home():
        return "hello world"

    return app


def create_celery(app=None):
    app = app or create_flask()
    # setup celery
    celery = Celery(app.name, broker=getenv('REDIS_URL'))
    task_base = celery.Task

    class ContextTask(task_base):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return task_base.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery


celery_app = create_celery()
