from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(token, password):
    uid = verify_auth_token(token)
    print('uid is', uid)
    return True

def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise userError()
    except SignatureExpired:
        raise userError()
    uid = data['uid']
    return uid