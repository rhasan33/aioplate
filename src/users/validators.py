from typing import Dict

from users.objects import USER


def registration_validator(request_body: Dict) -> bool:
    if set(USER.keys()) != set(request_body.keys()):
        return False
    for key in request_body.keys():
        try:
            USER[key]['value'] = request_body[key]
            if not type(USER[key]['value']) == USER[key]['type']:
                return False
            if USER[key]['required'] and not request_body[key]:
                return False
        except KeyError:
            return False
