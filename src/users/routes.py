from aiohttp import web

from users.views import registration

admin_routes = [
    web.post('/api/v1/users/registration', registration)
]

user_routes = admin_routes
