from typing import Dict, Union

from users.models import User


def create_user(data: Dict) -> Union[User, bool]:
    try:
        User.get(User.username == data['username'])
        return False
    except User.DoesNotExist:
        user = User()
        user.username = data['username']
        user.password = user.set_password(raw_password=data['password'])
        user.is_active = True
        user.tags = data.get('tag', list())
        user.name = data['name']
        user.email = data['email']
        user.save()
        return user
