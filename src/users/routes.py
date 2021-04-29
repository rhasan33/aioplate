from aiohttp import web

from configs import V1_PATTERNS
from users.views import UserListCreateView


common_routes = [
    web.view(f'{V1_PATTERNS}/user', UserListCreateView)
]

user_routes = common_routes
