from aiohttp import web

from users.validators import user_create_validation


class UserListCreateView(web.View):
    @user_create_validation
    async def post(self):
        data = {
            'name': 'Rakib Hasan Amiya'
        }
        return web.json_response(data=data, status=201)
