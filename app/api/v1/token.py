from app.libs.redprint import Redprint
from app.models.traveller import Traveller
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import jsonify, current_app
api = Redprint('token')

@api.route('/login', methods=['POST'])
def get_token():
    res = Traveller.verify(request.json['email'], request.json['password'])
    token = generate_auth_token(res['uid'])
    t = {'token': token}
    return jsonify(t)

def generate_auth_token(uid, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
    return s.dumps({
        'uid':uid
    }).decode('ascii')