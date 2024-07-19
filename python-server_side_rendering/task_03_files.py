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
    file_type = request.args.get("source")
    id = request.args.get("id")
    
    if file_type == "json":
        with open("products.json", "r") as json_file:
            data = json.load(json_file)
        if id:
            bandera = False
            for dictionary in data:
                if str(dictionary["id"]) == id:
                    data = []
                    data.append(dictionary)
                    bandera = True
            if not bandera:
                data = 1
    elif file_type == "csv":
        with open ("products.csv", newline="") as csv_file:
            data = csv.DictReader(csv_file)
            data = list(data)
        if id:
            bandera = False
            for row in data:
                if str(row["id"]) == id:
                    data = []
                    data.append(row)
                    bandera = True
            if not bandera:
                data = 1
    else:
        data = []
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)