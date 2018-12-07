from aiohttp import web


async def init_app(loop):
    app = web.Application(loop=loop, middlewares=[])
    app.router.add_post('/api/v1', handler)
    return app