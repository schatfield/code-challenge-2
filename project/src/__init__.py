from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import config
from . import app

# INIT DB
db = SQLAlchemy(app)

#INIT MARSHMALLOW
ma = Marshmallow(app)


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()
    return flask_app