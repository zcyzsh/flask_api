from .app import Flask
from flask.json import jsonify

# ---->please import model package in this section <----#
from app.models.hotel import Hotel

# ---->please import model package in this section <----#

from app.models.base import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')

    db.init_app(app)
    db.create_all(app=app)

    register_blueprint(app)

    return app

def register_blueprint(app):
    from app.api.v1 import create_blueprint_v1
    app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')
    