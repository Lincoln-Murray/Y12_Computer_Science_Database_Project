from flask import Flask, render_template, request
import requests as r
import sqlite3

app = Flask(__name__)


_products = []

@app.route("/<string:sort>", methods=['GET','POST'])
def index(sort):
    print(sort)
    conn = sqlite3.connect('sqlite (2).db')
    curs = conn.cursor()
    if sort == 'price-min':
        with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read()[:-1] + " order by 'productssupplier'.price ASc;")
        for line in curs:
            _products.append(line)
    if sort == 'price-max':
        with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read()[:-1] + " order by 'productssupplier'.price DESC;")
        for line in curs:
            _products.append(line)
    else:
        with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read())
        for line in curs:
            _products.append(line)
    conn.commit()
    conn.close()
    #print(render_template('index.html', products = _products))
    return render_template('index.html', products = _products)

@app.route("/product<int:product_id>", methods=['GET','POST'])
def product(product_id):
    conn = sqlite3.connect('sqlite (2).db')
    curs = conn.cursor()
    with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read()[:-1] + " where 'products'.'product_id' = " + str(product_id) + ";")
    for line in curs:
        _product = line
    print(_products)
    conn.commit()
    conn.close()
    return render_template('product.html', product = _product)
