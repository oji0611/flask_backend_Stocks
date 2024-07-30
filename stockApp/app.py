from flask import Flask
from flask.json import jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from stockApp.models.database import db
from stockApp.blueprints.products.detail import entry_list as entry
from stockApp.blueprints.products.index import product_list as product
import logging


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///warehouse.db'
db.init_app(app)
with app.app_context():
  db.create_all()
  
@app.route('/')
def index():
    return jsonify({'massage 1': 'vous êtes sur la landing page de mon application de gestion de stock', 'message 2': 'ici vous pouvez voir la liste des produits référencés et leurs stock mais aussi le détail des mouvemnts de stock'})
  
app.register_blueprint(product)#, url_prefix='/admin')