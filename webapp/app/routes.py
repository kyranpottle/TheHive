from flask import render_template

from app import app
# from app import mongo
from app import socket

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')