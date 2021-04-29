import functools
from typing import Callable


def user_create_validation(func: Callable):
    @functools.wraps(func)
    async def wrapper(cls, *args, **kwargs):
        # session = await get_session(cls.request)
        print(await cls.request.json())
        return await func(cls, *args, **kwargs)
    return wrapper
