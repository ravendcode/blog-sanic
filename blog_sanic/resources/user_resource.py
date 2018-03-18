from sanic import Blueprint
from utils.response import ok_json, error_json, not_found_abort


class User:
    def __init__(self, id, username, email):
        self.id = id
        self.username = username
        self.email = email


storage = [User(1, 'root', 'root@email.com'),
           User(2, 'bob', 'bob@email.com')]

api = Blueprint('user', url_prefix='/api')


async def findByParam(id):
    for user in storage:
        if user.id == id:
            return user
    not_found_abort('Not Found User')


@api.route('/user', methods=['GET'])
async def getAll(request):
    return ok_json('getAll', storage)


@api.route('/user', methods=['POST'])
async def createOne(request):
    if not request.json.get('email'):
        return error_json(errors={'email': 'required'}, status=400)
    user = User(len(storage) + 1, request.json.get('username'), request.json.get('email'))
    storage.append(user)
    return ok_json('createOne', user, 201)


@api.route('/user/<id:int>', methods=['GET'])
async def getOne(requestm, id):
    user = await findByParam(id)
    return ok_json('getOne', user)


@api.route('/user/<id:int>', methods=['PATCH'])
async def updateOne(request, id):
    user = await findByParam(id)
    if request.json.get('username'):
        user.username = request.json.get('username')
    if request.json.get('email'):
        user.email = request.json.get('email')
    return ok_json('updateOne', user)


@api.route('/user/<id:int>', methods=['DELETE'])
async def deleteOne(request, id):
    user = await findByParam(id)
    storage.remove(user)
    return ok_json('deleteOne', user)
