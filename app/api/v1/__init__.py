from flask import Blueprint
from app.api.v1 import hotel
def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    hotel.api.register(bp_v1)
    return bp_v1