import os
from sanic import Sanic
from sanic import response
from sanic.exceptions import NotFound
from dotenv import load_dotenv
from config import routes
import ws


load_dotenv()

ENV = os.getenv('ENV', 'production')
PORT = os.getenv('PORT', 80)
DEBUG = ENV != 'production'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
NODE_MODULES_DIR = os.path.join(BASE_DIR, 'node_modules')

print('ENV is {}'.format(ENV))

app = Sanic(__name__)

app.static('/static', STATIC_DIR)
app.static('/node_modules', NODE_MODULES_DIR)


@app.exception(NotFound)
async def not_found(request, exception):
    return await response.file(os.path.join(STATIC_DIR, 'index.html'))


@app.route("/")
async def home(request):
    return await response.file(os.path.join(STATIC_DIR, 'index.html'))

routes.init(app)
ws.init(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)
