from typing import Dict

from users.models import User


class UserSerializer(object):
    @staticmethod
    def format(obj: User) -> Dict:
        data = {
            'name': obj.name,
            'username': obj.username,
            'email': obj.email,
            'tags': obj.tags,
        }
        return data
