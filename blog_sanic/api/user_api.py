from sanic.response import json
from sanic import Blueprint

api = Blueprint('user')


@api.route('/')
async def bp_root(request):
    return json({'message': 'getAllUser'})
