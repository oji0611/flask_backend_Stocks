from flask import Blueprint
from flask import request, jsonify, make_response, redirect
from stockApp.models.database import db
from stockApp.models.products import Product
from stockApp.models.entry import Entry

entry_list = Blueprint('entry', __name__)

@entry_list.route('/product/<int:id>', methods=['GET'])
def entry_get(id): 
  entries = Entry.query.filter_by(productid=id).order_by(Entry.entrydate).all()

  return jsonify(entries) 

@entry_list.route('/product/<int:id>', methods=['POST'])
def entry_post(id):
  requestdata = request.json
  entrydate = requestdata['entrydate']
  productid = requestdata['productid']
  quantity = requestdata['quantity']
  mov_type = requestdata['mov_type']
  entry = Entry(entrydate=entrydate, productid=productid, quantity=quantity, mov_type=mov_type)
  db.session.add(entry)
  db.session.commit()
  return 'ok', 201

@entry_list.route('/product/<int:id>', methods=['PUT'])
def entry_put(id): 
  entryid = request.form.get('entryid')
  entrydate = request.form.get('entrydate')
  productid = request.form.get('productid')
  quantity = request.form.get('quantity')
  mov_type = request.form.get('mov_type')
  entry = Entry(entryid=entryid,
                entrydate=entrydate,
                productid=productid,
                quantity=quantity,
                mov_type=mov_type)
  db.session.add(entry)
  db.session.commit()
  return redirect(url_for('entry_list'))

@entry_list.route('/product/<int:id>', methods=['DELETE'])
def entry_delete(id): 
  entryid = request.form.get('entryid')
  entry = Entry.query.filter_by(entryid=entryid).first()
  db.session.delete(entry)
  db.session.commit()
  return redirect(url_for('entry_list'))