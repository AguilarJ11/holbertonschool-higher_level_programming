#!/usr/bin/python3

from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "unapapalapass"
jwt = JWTManager(app)


users = {
      "user1": 
          {"username": "user1", "password": generate_password_hash("pass"), "role": "user"},
      "admin1": 
          {"username": "admin1", "password": generate_password_hash("pass"), "role": "admin"}
        }

@auth.verify_password
def verify_password(username, password):
    if username in users and \
        check_password_hash(users.get(username).get("password"), password):
        return True
    return False

@app.route("/basic-protected")
@auth.login_required
def basic_auth():
    return jsonify("Basic Auth: Access Granted"), 200

@app.route("/login", methods=["POST"])
def login():
    login_data = request.get_json()
    username = login_data.get("username")
    password = login_data.get("password")
    
    if username in users and check_password_hash(users[username]["password"], password):
        access_token = create_access_token(identity=login_data)
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_acccess():
    return jsonify("JWT Auth: Access Granted"), 200
        
@app.route("/admin-only")
@auth.login_required
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return jsonify("Admin Access: Granted"), 200
    else:
        return jsonify("403 Forbidden"), 403
    
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

app.run()