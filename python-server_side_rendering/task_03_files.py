#!/usr/bin/python3

from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open("items.json", "r") as file:
        data = json.load(file)
    if data:
        items = data["items"]
    else:
        items = []
    return render_template('items.html', items=items)

@app.route('/products')
def products():
    file_type = request.args("source")
    id = request.args("id")
    
    if file_type == "json":
        with open("products.json", "r") as json_file:
            data = json.load(json_file)
        if id:
            for dictionary in data:
                if dictionary["id"] == id:
                    data = dictionary
    elif file_type == "csv":
        with open ("products.csv", newline="") as csv_file:
            data = csv.DictReader(csv_file)
        if id:
            for col in data:
                if col["id"] == id:
                    csv_dict = {"name": col["name"],
                                "category": col["category"],
                                "price": col["price"]}
                    data = csv_dict
    else:
        data = []
    return render_template('items.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)