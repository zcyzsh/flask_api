from werkzeug.exceptions import HTTPException
from flask import request, json
class APIException(HTTPException):
    # 这个状态码在浏览器中
    code = 500
    msg = 'sorry'
    # 自定义错误码 以json格式返回
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        if code:
            self.code = code
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None, scope=None):
        body = dict(
            msg = self.msg,
            error_code = self.error_code,
            request = request.method + ' ' + self.get_url_no_param()
        )
        text = json.dumps(body)
        return text
    def get_headers(self, environ=None, scope=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]