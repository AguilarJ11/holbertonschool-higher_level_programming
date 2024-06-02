#!/usr/bin/python3

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return"OK"

@app.route("/users/<username>")
def user(username):
    
    if username in users.keys():
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json("username")
    username = data.get("username")
    
    if not username:
        return jsonify({"error": "username is required"}), 400
    
    users[username] = data
    msj_dict = {"message": "User added", "user": data}

    return jsonify(msj_dict), 201

if __name__ == "__main__": 
    app.run(debug=True)