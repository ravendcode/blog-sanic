from api import user_api, post_api


def init(app):
    app.blueprint(user_api.api, url_prefix='/api/user')
    app.blueprint(post_api.api, url_prefix='/api/post')
