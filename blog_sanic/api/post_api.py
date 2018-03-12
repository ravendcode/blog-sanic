from sanic.response import json
from sanic import Blueprint

api = Blueprint('post')


@api.route('/')
async def getAll(request):
    return json({'message': 'getAllPost'})
