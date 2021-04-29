import functools
from typing import Callable, Dict

from aiohttp import web

from base.validation_obj import USER


def user_create_validation(func: Callable):
    @functools.wraps(func)
    async def wrapper(cls, *args, **kwargs):
        body: Dict = await cls.request.json()
        required_keys = [key for key in USER.keys() if USER[key]['required']]
        checked_keys = []
        for key in body.keys():
            try:
                if not isinstance(body[key], USER[key]['type']):
                    return web.HTTPBadRequest(text=f'invalid data type for {key}')
                if USER[key]['required'] and not isinstance(body[key], bool) and not body[key]:
                    return web.HTTPBadRequest(text=f'invalid data for {key}')
                checked_keys.append(key)
            except KeyError:
                return web.HTTPBadRequest(text=f'invalid request key {key}')
        if required_keys > checked_keys:
            return web.HTTPBadRequest(text='not all necessary keys are provided')
        return await func(cls, *args, **kwargs)
    return wrapper
