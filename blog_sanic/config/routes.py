from resources import user_resource, post_resource


def init(app):
    app.blueprint(user_resource.api)
    app.blueprint(post_resource.api)
