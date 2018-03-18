from sanic import exceptions
from sanic.response import json


def not_found_abort(text='Not Found'):
    exceptions.abort(404, text)


def ok_json(message=None, data=None, status=200):
    status_text = None
    if status == 200:
        status_text = 'OK'
    if status == 201:
        status_text = 'Created'
    result = {
        'status_code': status,
        'status': status_text,
    }
    if message:
        result['message'] = message
    if data:
        result['data'] = data
    return json(result, status=status)


def error_json(message=None, errors=None, status=400):
    status_text = None
    if status == 400:
        status_text = 'Bad Request'
        message = message if message else 'Validation Error'
    if status == 401:
        status_text = 'Unauthorized'
        message = message if message else 'Unauthorized'
    if status == 402:
        status_text = 'Payment Required'
        message = message if message else 'Payment Required'
    if status == 403:
        status_text = 'Forbidden'
        message = message if message else 'Forbidden'
    if status == 404:
        status_text = 'Not Found'
        message = message if message else 'Not Found'
    if status == 405:
        status_text = 'Method Not Allowed'
        message = message if message else 'Method Not Allowed'
    if status == 500:
        status_text = 'Internal Server Error'
        message = message if message else 'Internal Server Error'
    result = {
        'status_code': status,
        'status': status_text,
        'message': message,
    }
    if errors:
        result['errors'] = errors
    return json(result, status=status)
