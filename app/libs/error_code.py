# 定义具体的异常报错
from app.libs.error import APIException


class NoException(APIException):
    code = 200
    msg = (
        'It works well.'
    )
    error_code = 200


class TestError(APIException):
    code = 400
    msg = (
        'this is error description'
    )


class ServerError(APIException):
    code = 500
    msg = (
        'It seems something unexpect happened >-<|'
    )


class ParameterException(APIException):
    code = 600
    msg = (
        '表单信息有误'
    )
    error_code = 600
