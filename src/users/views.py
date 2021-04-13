from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp import web

from users.validators import registration_validator


async def registration(request: Request) -> Response:
    data = await request.json()
    registration_validator(data)
    return web.json_response(data=data, status=201)
