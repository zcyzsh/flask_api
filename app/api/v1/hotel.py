from app.libs.redprint import Redprint

api = Redprint('hotel')

@api.route('/get', methods=['GET'])
def get_hotel():
    return 'hotel!!!'