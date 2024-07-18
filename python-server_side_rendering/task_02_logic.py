#!/usr/bin/python3

from flask import Flask, render_template, request

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

@app.route('/items', method=['GET'])
def contact():
    data = request.json()
    return render_template('items.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)