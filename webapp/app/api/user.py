import uuid

from flask import request, jsonify, make_response

from app import app, mongo
from app.api import logged_in_sessions

def user_is_logged_in(session_id):
    return session_id in logged_in_sessions

def get_user_from_session(session_id):
    return logged_in_sessions.get(session_id)
    
@app.route('/api/user/signup', methods=['POST'])
def signup_user():
    body = request.get_json()
    try:
        user = {
            'email': body['email'],
            'password': body['password']
        }
        mongo.db.users.insert_one(user)
        return 'Success'
    except KeyError:
        return "Invalid JSON body!", 400

@app.route('/api/user/login', methods=['POST'])
def login_user():
    body = request.get_json(force=True)
    try:
        user = {
            'email': body['email'],
            'password': body['password']
        }
        found_user = mongo.db.users.find_one(user)
        if found_user != None:
            if not request.cookies.get('username'):
                resp = make_response("Success", 200)
                resp.set_cookie('username', user['email'])
                return resp
            else:
                return "User already logged in!"
        else:
            return "No User Found", 400
    except KeyError:
        return "Invalid JSON body!", 400
