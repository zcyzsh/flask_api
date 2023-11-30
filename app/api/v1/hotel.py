from app.libs.redprint import Redprint
from app.libs.error_code import Error

api = Redprint('hotel')

@api.route('/get', methods=['GET'])
def get_hotel():
    raise Error()
    return 'hotel!!!'