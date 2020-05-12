# 定义具体的异常报错
from app.libs.error import APIException


class NoException(APIException):
    error_code = 200
    msg = (
        'It works well.'
    )


class TestError(APIException):
    error_code = 400
    msg = (
        'this is error description'
    )


class AuthorizationException(APIException):
    error_code = 403
    msg = (
        'No operation permission!'
    )


class ServerError(APIException):
    error_code = 500
    msg = (
        'It seems something unexpect happened >-<|'
    )


class ParameterException(APIException):
    error_code = 600
    msg = (
        '表单信息有误'
    )
