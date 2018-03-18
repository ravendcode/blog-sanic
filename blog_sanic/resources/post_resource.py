from sanic.response import json
from sanic import Blueprint

api = Blueprint('post', url_prefix='/api')


@api.route('/post', methods=['GET'])
async def getAll(request):
    return json({'message': 'getAllPost'})


@api.route('/post', methods=['POST'])
async def createOne(request):
    return json({'message': 'createOne'})


@api.route('/post/<id:int>', methods=['GET'])
async def getOne(requestm, id):
    return json({'message': 'getOne'})


@api.route('/post/<id:int>', methods=['PATCH'])
async def updateOne(request, id):
    return json({'message': 'updateOne'})


@api.route('/post/<id:int>', methods=['DELETE'])
async def deleteOne(request, id):
    return json({'message': 'deleteOne'})
