from d_views import index


def setup_routes(app):
    app.router.add_get('/', index)
    # app.router.add_get('/', 'test')
