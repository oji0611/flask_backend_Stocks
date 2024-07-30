from flask import Blueprint
from flask import request, jsonify, make_response
from stockApp.models.database import db
from stockApp.models.products import Product
from stockApp.models.entry import Entry
import logging


product_list = Blueprint('product', __name__)

@product_list.route('/product', methods=['GET'])
def products_get():
    products = Product.query.order_by(Product.productid).all()
    logging.warning(products)
    for product in range(len(products)):
        entries = Entry.query.filter_by(productid=products[product].productid).all()
        total = 0
        for entrie in entries:
            if entrie.mov_type == 'in':
                total += entrie.quantity
            else:
                total -= entrie.quantity
        products[product] = {'produit': products[product], 'total': total}
    return jsonify(products), 200

@product_list.route('/product', methods=['POST'])
def products_post():
    requestdata = request.json
    category = requestdata['category']
    unit = requestdata['unit']
    libele = requestdata['libele']
    product = Product(category=category, unit=unit, libele=libele)
    db.session.add(product)
    db.session.commit()
    return 'ok', 201

@product_list.route('/product', methods=['PUT'])
def products_put():
    requestdata = request.json
    productid = requestdata['productid']
    category = requestdata['category']
    unit = requestdata['unit']
    libele = requestdata['libele']
    product = Product.query.filter_by(productid=productid).first()
    product.productid = productid
    product.category = category
    product.unit = unit
    product.libele = libele
    db.session.commit()
    return 'ok', 204

@product_list.route('/product', methods=['DELETE'])
def products_delete():
    requestdata = request.json
    productid = requestdata['productid']
    product = Product.query.filter_by(productid=productid).first()
    db.session.delete(product)
    db.session.commit()
    return 'ok', 204

