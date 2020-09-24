import flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#DB
db = SQLAlchemy(app)

#MARSHMALLOW
ma = Marshmallow(app)


# CLASS/MODEL
class BudgetItem(db.Model):
    __tablename__ = "budget item"

    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(128), unique=True, nullable=False)
    item_cost = db.Column(db.Integer, unique=True, nullable=False)
    total_budget = db.Column(db.Integer, unique=True, nullable=False)
    avail_budget = db.Column(db.Integer, unique=True, nullable=False)

    # def __init__(self, email):
    #     self.email = email


class BudgetItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'item_name', 'item_cost', 'avail_budget', 'total_budget')

# MARSHMALLOW SCHEMA INSTANCES
budget_item_schema = BudgetItemSchema()
budget_items_schema = BudgetItemSchema(many=True)    
