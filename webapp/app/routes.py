from flask import render_template

from app import app
# from app import mongo
from app import socket

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/rent')
def rentPage():
    return render_template('rent.html')

@app.route('/host')
def hostPage():
    return render_template('host.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/signup')
def signupPage():
    return render_template('signup.html')

@app.route('/editor')
def editorPage():
    return render_template('editor.html')
