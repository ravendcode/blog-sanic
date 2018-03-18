from sanic import Sanic
from config import routes, config
import handlers
import ws

app = Sanic(__name__)

app.static('/static', config.STATIC_DIR)
app.static('/node_modules', config.NODE_MODULES_DIR)

handlers.init(app)
routes.init(app)
ws.init(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG)
