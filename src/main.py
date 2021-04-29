import asyncio
import logging
from typing import Dict

from aiohttp import web
from aiohttp.web import Application, json_response, run_app
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp_middlewares import cors_middleware
from aiohttp_middlewares.cors import DEFAULT_ALLOW_HEADERS

import aio_pika
import aioredis

from configs import DEBUG, RABBITMQ_URL, REDIS_HOST, db
from middleware import render
from users.routes import user_routes

loop = asyncio.get_event_loop()

logger = logging.getLogger(__name__)


async def health_check(request: Request) -> Response:
    data: Dict = {
        'message': 'aiohttp boilerplate with postgres, redis and rabbitmq',
        'data': {
            'request_method': request.method.lower(),
        }
    }
    return json_response(data=data, status=200)


async def on_start_up(application: Application):
    try:
        logger.info('rabbitmq connection stated')
        application['rabbit'] = await aio_pika.connect_robust(url=RABBITMQ_URL, loop=loop)
        logger.info('rabbitmq connection completed')
        logger.info('redis connection stated')
        application['redis'] = await aioredis.create_pool(address=REDIS_HOST)
        logger.info('redis connection completed')
        logger.info('db connection stated')
        db.connect()
        application['db'] = db
        logger.info('db connection completed')
    except (ConnectionError, Exception):
        logger.info('trying to establish connection after 2 sec')
        await asyncio.sleep(2)


async def on_app_close(application: Application):
    try:
        if application['rabbit']:
            await application['rabbit'].close()
            logger.info('rabbitmq connection closed')
        await application['redis'].close()
        await application['redis'].wait_closed()
        logger.info('redis connection closed')
        application['db'].close()
        logger.info('db connection closed')
    except (Exception, ConnectionError) as e:
        logger.info(f'trying to reconnect: {e}')
        await asyncio.sleep(2)

app = Application(
    middlewares=[
        render,
        cors_middleware(
            allow_all=True,
            allow_headers=DEFAULT_ALLOW_HEADERS + ('SECRET-KEY',)
        ),
    ]
)
app.on_startup.append(on_start_up)
app.on_shutdown.append(on_app_close)

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)

app.add_routes([web.get('/', health_check)])
app.add_routes(user_routes)

if not DEBUG:
    run_app(app=app, port=8030)
