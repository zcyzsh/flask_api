from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from flask import request
from flask import jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from app.models.base import db
from app.models.traveller import Traveller
from app.libs.error_code import Error
from app.spider.xiaosuplan import route_plan
api = Redprint('traveller')

@api.route('/register', methods=['POST'])
def trabeller_register():
    print(type(request.json))
    with db.auto_commit():
        traveller = Traveller()
        traveller.nickname = request.json['nickname']
        traveller.email = request.json['email']
        traveller.password = request.json['password']
        db.session.add(traveller)
    return {"code": 200, "msg": "success"}

@api.route('/change', methods=['GET'])
def trabeller_change():
    traveller = Traveller.query.filter_by(email='1589872509@qq.com').first()
    with db.auto_commit():
        traveller.nickname = "苏苏的小鼠"
    return '小苏旅游修改'

@api.route('/search', methods=['GET'])
def trabeller_search():
    traveller = Traveller.query.filter_by(email='1589872509@qq.com').first()
    return jsonify(traveller)


@api.route('/login', methods=['POST'])
def get_token():
    res = Traveller.verify(request.json['email'], request.json['password'])
    print(res['uid'])
    token = generate_auth_token(res['uid'])
    t = {'token': token}
    return jsonify(t)

def generate_auth_token(uid, scope=None, expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
    return s.dumps({
        'uid': uid
    }).decode('ascii')

@api.route('/error', methods=['GET'])
def trabeller_error():
    raise Error()
    return '小苏旅游修改'

@api.route('/verify', methods=['GET'])
@auth.login_required
def route():
    return {'msg': 'token验证成功'}
