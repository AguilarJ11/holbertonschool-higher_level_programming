#!/usr/bin/python3

from flask import Flask, jsonify
import json

app = Flask(__name__)

users = {"jose":{"name":"Jose", "age": 70, "city": "Montevideo"},
             "pepe":{"name":"pepe", "age": 45, "city": "Bs As"},}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/status")
def status():
    return"OK"

@app.route("/user/<username>", methods=["GET"])
def user(username):
    if username in users.keys():
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})

@app.route("/add_user/<new_user>", methods=["POST"])
def add_user(new_user):
    data = json.loads(new_user)
    username = data.get("username")
    
    if username in users.keys():
        return "User name already exists"
    else:
         users[username] = data
         msj_dic = {"message": "User added",
                    username: data}
         return jsonify(msj_dic)

if __name__ == "__main__": 
    app.run(debug=True)