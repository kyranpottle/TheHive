import logging

from flask import Flask
from flask_socketio import SocketIO
from flask_pymongo import PyMongo

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
app.config.from_pyfile('settings.cfg')

socketio = SocketIO(app, async_mode="eventlet", async_handlers=True)
mongo = PyMongo(app)

from app import socket
from app import routes
from app import api