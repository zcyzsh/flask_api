from werkzeug.exceptions import HTTPException
from app.libs.error import APIException
class Error(APIException):
    code = 400
    error_code = 1006
    msg = '错误'
class userError(APIException):
    code = 400
    error_code = 1007
    msg = '用户错误'
class planError(APIException):
    code = 400
    err_code = 1008
    msg = '无法进行规划'