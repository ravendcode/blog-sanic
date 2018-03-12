import json
import asyncio


connections = set()


def init(app):
    @app.websocket('/echo')
    async def feed(request, ws):
        try:
            global connections
            connections.add(ws)
            print(connections)
            await ws.send(json.dumps({'type': 'server', 'data': 'hello'}))
            while True:
                data = await ws.recv()
                await asyncio.wait([ws.send(data) for ws in connections])
        finally:
            connections.remove(ws)
            print(connections)
        # async for message in ws:
        #     await ws.send(message)
        # while True:
        #     # data = 'hello!'
        #     # await ws.send(data)
        #     data = await ws.recv()
        #     print('Received: ' + data)
        #     await ws.send(data)
        #     print('Sending: ' + data)
