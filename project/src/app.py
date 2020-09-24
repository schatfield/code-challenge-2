
import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask import Flask, request, jsonify
import json
from . import create_app
from .models import BudgetItem, BudgetItemSchema

# def create_app():
#     flask_app = Flask(__name__)
#     flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
#     flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     flask_app.app_context().push()
#     db.init_app(flask_app)
#     db.create_all()
#     return flask_app

app = create_app()

# MARSHMALLOW SCHEMA INSTANCES
budget_item_schema = BudgetItemSchema()
budget_items_schema = BudgetItemSchema(many=True)    

# ENDPOINTS

@app.route('/')
def hello():
    return "Hello World!"

# GET (Retrieve)
@app.route('/budget_item/')
def budget_item_list():
    all_budget_items = BudgetItem.query.all()
    return jsonify(budget_items_schema.dump(all_budget_items))

# POST (Create)
@app.route('/budget_item/', methods=['POST'])
def create_budget_item():
    print("HELLO")
    item_name = request.json.get('item_name', '')
    item_cost = request.json.get('item_cost', '')
    avail_budget = request.json.get('avail_budget', '')
    
    new_item = BudgetItem(item_name=item_name, item_cost=item_cost, avail_budget=avail_budget)

    db.session.add(new_item)
    db.session.commit()

    return budget_item_schema.jsonify(new_item)

# GET ONE
@app.route('/budget_item/<int:item_id>/', methods=["GET"])
def single_budget_item(item_id):
    single_item = BudgetItem.query.get(item_id)
    return budget_item_schema.jsonify(single_item)

# UPDATE (Edit)
@app.route('/budget_item/<int:item_id>/', methods=['PATCH'])
def update_budget_item(item_id):
    item_name = request.json.get('item_name', '')
    item_cost = request.json.get('item_cost', '')
    avail_budget = request.json.get('avail_budget', '')

    item = BudgetItem.query.get(item_id)
    
    item.item_name = item_name
    item.item_cost = item_cost
    item.avail_budget = avail_budget

    db.session.add(item)
    db.session.commit()

    return budget_item_schema.jsonify(item)

# DELETE 
@app.route('/budget_item/<int:item_id>/', methods=["DELETE"])
def delete_budget_item(item_id):
    item = BudgetItem.query.get(item_id)

    db.session.delete(item)
    db.session.commit()

    return budget_item_schema.jsonify(item)




