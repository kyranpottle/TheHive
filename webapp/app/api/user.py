import uuid

from flask import request, jsonify

from app import app, mongo
from app.api import valid_tokens

def create_user_token():
    return uuid.uuid4().hex
    
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
    body = request.get_json()
    try:
        user = {
            'email': body['email'],
            'password': body['password']
        }
        found_user = mongo.db.users.find_one(user)
        if found_user != None:
            return create_user_token()
        else:
            return "No User Found", 400
    except KeyError:
        return "Invalid JSON body!", 400
