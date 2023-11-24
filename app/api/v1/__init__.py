from flask import Blueprint
from app.api.v1 import sudo
from app.api.v1 import plan
from app.api.v1 import traveller
def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    traveller.api.register(bp_v1)
    sudo.api.register(bp_v1)
    plan.api.register(bp_v1)
    return bp_v1