from aiohttp import web

from users.validators import user_create_validation
from users.repositories import create_user
from users.serializers import UserSerializer


class UserListCreateView(web.View):
    @user_create_validation
    async def post(self):
        request_body = await self.request.json()
        user = create_user(data=request_body)
        if not user:
            return web.HTTPConflict(text='user already exists')
        serializer = UserSerializer()
        return web.json_response(data=serializer.format(user), status=201)
