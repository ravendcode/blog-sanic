from sanic import exceptions
from sanic.response import json


def not_found_abort(text='Not Found'):
    exceptions.abort(404, text)


def ok_json(message=None, data=None, status_code=200):
    if status_code == 200:
        status = 'OK'
    if status_code == 201:
        status = 'Created'
    result = {
        'status_code': status_code,
        'status': status,
    }
    if message:
        result['message'] = message
    if data:
        result['data'] = data
    return json(result, status=status_code)


def error_json(message=None, errors=None, status_code=400):
    if status_code == 400:
        status = 'Bad Request'
        message = message if message else 'Validation Error'
    if status_code == 401:
        status = 'Unauthorized'
        message = message if message else 'Unauthorized'
    if status_code == 402:
        status = 'Payment Required'
        message = message if message else 'Payment Required'
    if status_code == 403:
        status = 'Forbidden'
        message = message if message else 'Forbidden'
    if status_code == 404:
        status = 'Not Found'
        message = message if message else 'Not Found'
    if status_code == 405:
        status = 'Method Not Allowed'
        message = message if message else 'Method Not Allowed'
    if status_code == 500:
        status = 'Internal Server Error'
        message = message if message else 'Internal Server Error'
    result = {
        'status_code': status_code,
        'status': status,
        'message': message,
    }
    if errors:
        result['errors'] = errors
    return json(result, status=status_code)
