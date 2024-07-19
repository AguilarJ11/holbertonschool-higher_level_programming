#!/usr/bin/python3

from flask import Flask, render_template, request
import json, csv, sqlite3
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
db = SQLAlchemy(app)

class Products(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False) 
    price = db.Column(db.Float(50), nullable=False)

def create_database_alchemy():
    with app.app_context():
        db.create_all()
    new_product_one = Products(name="Laptop", category="Electronics", price=799.99)
    new_product_two = Products(name="Coffee Mug", category="Home Goods", price=15.99)
    db.session.add(new_product_one)
    db.session.add(new_product_two)
    db.session.commit()

def create_database_sqlite3():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

"""
Endpoints
"""

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
    persistence_type = request.args.get("source")
    id = request.args.get("id")
    
    if persistence_type == "json":
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

    elif persistence_type == "csv":
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

    elif persistence_type == "sql_alchemy":
        create_database_alchemy()
        if id:
            try:
                data_query = db.session.get(Products, id)
                data = []
                data.append(data_query)
            except Exception as e:
                print(e)
        else:
            data_query = db.session.query(Products).all()
            data = []
            for products in data_query:
                data.append(products)

    elif persistence_type == "sql":
        if id:
            create_database_sqlite3()
            conn = sqlite3.connect('products.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * from Products")
            data_query = cursor.fetchall()
            keys_list = []
            for keys in cursor.description:
                keys_list.append(keys[0])

  
    else:
        data = []
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)