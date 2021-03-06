
from werkzeug.exceptions import HTTPException
from app.libs.error import APIException


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class DeleteSuccess(Success):
    code = 202
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = 'a server error ocur'
    error_code = 999

class ClientTypeError(APIException):
    code = 400
    msg = 'client sign_type is invalid'
    error_code = 1006


class ParameterException(APIException):
    code = 400
    msg = 'invalid parameter'
    error_code = 1000


class NotFound(APIException):
    code = 404
    msg = 'the recourse are not found'
    error_code = 1001


class AuthFailed(APIException):
    code = 401
    msg = 'authorization failed'
    error_code = 1002

class Forbidden(APIException):
    code = 403
    error_code = 1004
    msg = 'forbidden, not in scope'
