import json
import asyncio


connections = set()


def init(app):
    @app.websocket('/echows')
    async def feed(request, ws):
        try:
            global connections
            connections.add(ws)
            print(connections)
            await ws.send(json.dumps({'type': 'server:hello',
                                      'data': 'hello'}))
            while True:
                data = await ws.recv()
                await asyncio.wait([ws.send(data) for ws in connections])
        finally:
            connections.remove(ws)
            print(connections)
