from flask import Blueprint
from app.api.v1 import hotel
def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)

    #---->please add code in this section <----#
    hotel.api.register(bp_v1)

    #---->please add code in this section <----#

    return bp_v1