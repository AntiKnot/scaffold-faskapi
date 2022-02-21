from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.staticfiles import StaticFiles

from api.v1 import api_v1

description = """
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""


def create_app():
    app = FastAPI(
        title='ChimichangApp',
        description=description,
        version='0.0.1',
        terms_of_service='http://example.com/terms/',
        contact={
            'name': 'Deadpoolio the Amazing',
            'url': 'http://x-force.example.com/contact/',
            'email': 'dp@x-force.example.com',
        },
        license_info={
            'name': 'Apache 2.0',
            'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
        },
        router=api_v1,
        prefix='/api/v1/view',
    )
    app.mount('/static', StaticFiles(directory='static'), name='static')
    register_exception(app)
    register_middleware(app)
    # app.add_api_route()
    # app.add_middleware()
    # app.add_exception_handler()
    # app.add_api_websocket_route()
    # app.add_event_handler()
    # app.add_websocket_route()

    return app


def register_exception(app: FastAPI):
    """
    全局异常捕获
    :param app:
    :return:
    """

    @app.exception_handler(Exception)
    async def all_exception_handler(request: Request, exc: Exception):
        logger.error(
            f'全局异常\nURL:{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}'
        )
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                'code': 500,
                'data': {
                    'tip': '服务器错误'
                },
                'message': 'fail'
            },
        )


def register_middleware(app: FastAPI):

    @app.middleware('http')
    async def add_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers['X-Process-Time'] = str(process_time)
        return response
