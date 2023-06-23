#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from datetime import datetime
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = [
        {'id': 1, 'name': 'Bakery 1', 'created_at': datetime.utcnow()},
        {'id': 2, 'name': 'Bakery 2', 'created_at': datetime.utcnow()},
    ]
    
    return jsonify(bakeries)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = {'id': id, 'name': f'Bakery {id}', 'created_at': datetime.utcnow()}
    return jsonify(bakery)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods = [
        {'id': 1, 'name': 'Good 1', 'price': 10.99, 'created_at': datetime.utcnow()},
        {'id': 2, 'name': 'Good 2', 'price': 15.99, 'created_at': datetime.utcnow()},
    ]
    
    return jsonify(baked_goods)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_good = {
        'id': 1,
        'name': 'Expensive Good',
        'price': 99.99,
        'created_at': datetime.utcnow()
    }
    return jsonify(baked_good)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
