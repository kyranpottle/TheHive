from threading import Thread

from eventlet import event, spawn
from flask import request
from flask_socketio import join_room, leave_room, emit, disconnect

from app import socketio
# from app import mongo


@socketio.on('connect')
def on_connect():
    return

@socketio.on('disconnect')
def disconnect():
    return