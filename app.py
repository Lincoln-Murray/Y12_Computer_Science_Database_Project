from flask import Flask, render_template, request
import requests as r
import sqlite3

app = Flask(__name__)

_order_id = 1

@app.route("/s=<string:sort>&q=<string:query>", methods=['GET','POST'])
def index(sort, query):
    _products = []
    conn = sqlite3.connect('Rock Scalers.db')
    curs = conn.cursor()
    if query != 'null':
        search = "where 'products'.'product_name' like '%" + str(query) + "%'"
    else:
        search=''
    if sort == 'price-min':
        with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read().replace('group', search + "group")[:-1] + "order by 'productssupplier'.price ASC;")
        for line in curs:
            _products.append(line)
    if sort == 'price-max':
        with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read().replace('group', search + "group")[:-1] + "order by 'productssupplier'.price DESC;")
        for line in curs:
            _products.append(line)
    else:
        with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read().replace('group', search + "group"))
        for line in curs:
            _products.append(line)
    conn.commit()
    conn.close()
    if 'iphone' in request.headers.get('User-Agent').lower() or 'android' in request.headers.get('User-Agent').lower():
        return render_template('index_m.html', products = _products)
    else:
        return render_template('index.html', products = _products)

@app.route("/", methods=['GET','POST'])
def default_index():
    return index('relevance', 'null')

@app.route("/product<int:product_id>", methods=['GET','POST'])
def product(product_id):
    conn = sqlite3.connect('Rock Scalers.db')
    curs = conn.cursor()
    with open('sql/select_products.sql') as sql_select: curs.execute(sql_select.read().replace('group', " where 'products'.'product_id' = " + str(product_id) + " group"))
    for line in curs:
        _product = line
    conn.commit()
    conn.close()
    if 'iphone' in request.headers.get('User-Agent').lower() or 'android' in request.headers.get('User-Agent').lower():
        return render_template('product_m.html', product = _product)
    else:
        return render_template('product.html', product = _product)

@app.route("/cart/<int:order_id>")
def cart(order_id):
    global _order_id
    _order_id = order_id
    _products = []
    conn = sqlite3.connect('Rock Scalers.db')
    curs = conn.cursor()
    with open('sql/select_cart_products.sql') as sql_select: curs.execute(sql_select.read().replace(str(2), str(order_id)))
    for line in curs:
        _products.append(line)
    conn.commit()
    conn.close()
    conn = sqlite3.connect('Rock Scalers.db')
    curs = conn.cursor()
    with open('sql/select_order_summary.sql') as sql_select: curs.execute(sql_select.read().replace(str(-2), str(order_id)))
    for line in curs:
        _summary = line
    conn.commit()
    conn.close()
    if 'iphone' in request.headers.get('User-Agent').lower() or 'android' in request.headers.get('User-Agent').lower():
        return render_template('cart_m.html', products = _products, order_id = order_id, summary = _summary)
    else:
        return render_template('cart.html', products = _products, order_id = order_id, summary = _summary)

@app.route("/cart")
def default_cart():
    global _order_id
    return cart(_order_id)

@app.route("/remove_p=<int:product_id>&o=<int:order_id>", methods=['GET','POST'])
def remove_item(product_id, order_id):
    conn = sqlite3.connect('Rock Scalers.db')
    curs = conn.cursor()
    with open('sql/delete_product_from_order.sql') as sql_select: curs.execute(sql_select.read().replace(str(-1), str(product_id)).replace(str(-2), str(order_id)))
    conn.commit()
    conn.close()
    return cart(order_id)

@app.route("/add_p=<int:product_id>")
def add_item(product_id):
    global _order_id
    conn = sqlite3.connect('Rock Scalers.db')
    curs = conn.cursor()
    with open('sql/create_new_order.sql') as sql_select: curs.execute(sql_select.read().replace(str(-1), str(product_id)).replace(str(-2), str(_order_id)))
    conn.commit()
    conn.close()
    return cart(_order_id)

@app.errorhandler(404)
def page_not_found(error):
    if 'iphone' in request.headers.get('User-Agent').lower() or 'android' in request.headers.get('User-Agent').lower():
        return render_template('404_m.html', error_message=error)
    else:
        return render_template('404.html', error_message=error)
