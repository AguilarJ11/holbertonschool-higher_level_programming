#!/usr/bin/python3

from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
      "user1": {"username": "user1", "password": generate_password_hash("pass-user"), "role": "user"},
      "admin1": {"username": "admin1", "password": generate_password_hash("pass-admin"), "role": "admin"}
  }

@auth.verify_password
def verify_password(username, password):
    
@app.route("/basic-protected")
@auth.login_required(role="user")
def home():
    return jsoninfy("Basic Auth: Access Granted")

@app.route("/login", methods=["POST"])
login_data = request.get_json("user")
def home():


@app.route("/jwt-protected")
@auth.login_required
def jwt_acccess():
    return jsoninfy("JWT Auth: Access Granted")
        
@app.route("/admin-only")
@auth.login_required(role="admin")
def admin_only():
    return jsoninfy("Admin Access: Granted")