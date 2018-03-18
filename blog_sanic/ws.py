# import asyncio
import json
import uuid

connections = dict()


def add(ws):
    id = str(uuid.uuid4())
    connections[id] = ws
    return id


def remove(id):
    connections.pop(id)


async def broadcast(data):
    for id in connections:
        await connections[id].send(data)


def init(app):
    @app.websocket('/echows')
    async def feed(request, ws):
        try:
            id = add(ws)
            print('id', id)
            await ws.send(json.dumps({
                'id': id,
                'type': 'server:hello',
                'data': 'hello',
            }))
            while True:
                data = await ws.recv()
                print('data', data)
                await broadcast(data)
                # await asyncio.wait([ws.send(data) for ws in connections])
        finally:
            remove(id)
