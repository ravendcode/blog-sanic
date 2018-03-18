import os
import re
from sanic.exceptions import NotFound
from sanic import response
from config import config


def init(app):
    @app.exception(NotFound)
    async def not_found(request, exception):
        if re.findall(r'/api', request.url):
            result = {
                'status_code': 404,
                'status': 'Not Found',
                'message': str(exception)
            }
            return response.json(result, status=404)
        else:
            return await response.file(os.path.join(config.STATIC_DIR, 'index.html'))

    @app.route("/")
    async def home(request):
        return await response.file(os.path.join(config.STATIC_DIR, 'index.html'))

    @app.route("/echo")
    async def echo(request):
        return await response.file(os.path.join(config.STATIC_DIR, 'echo.html'))
