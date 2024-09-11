from flask import Flask, render_template, request
import requests as r
import sqlite3

app = Flask(__name__)


_products = []

@app.route("/")
def index():
    conn = sqlite3.connect('sqlite (2).db')
    curs = conn.cursor()
    with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read())
    for line in curs:
        _products.append(line)
    return render_template('index.html', products = _products)
