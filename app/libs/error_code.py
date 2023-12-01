from werkzeug.exceptions import HTTPException
from app.libs.error import APIException
class Error(APIException):
    code = 400
    error_code = 1006
    msg = '错误'