from app.libs.redprint import Redprint
from app.models.hotel import Hotel
from app.models.base import db
from flask.json import jsonify

api = Redprint('hotel')

@api.route('/get', methods=['GET'])
def get_hotel():
    return 'hotel!!!'

@api.route('/set', methods=['GET'])
def set_hotel():
    hotel = Hotel()
    with db.auto_commit():
        hotel.price = 348
        hotel.location = '南京'
        hotel.description = '位于6朝古都的南京'
        hotel.src = '如家'
        hotel.comments = '舒服的一次住宿'
        db.session.add(hotel)
    return 'hotel saved in db'




@api.route('/search', methods=['GET'])
def search_hotel():
    hotel = Hotel.query.filter_by(id=1).first()
    return jsonify(hotel)