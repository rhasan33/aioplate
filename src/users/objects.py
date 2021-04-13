USER = {
    'username': {
        'type': str,
        'required': True
    },
    'first_name': {
        'type': str,
        'required': True
    },
    'last_name': {
        'type': str,
        'required': True
    },
    'gender': {
        'type': str,
        'required': False
    },
    'is_active': {
        'type': bool,
        'required': False
    },
    'is_staff': {
        'type': bool,
        'required': False
    },
    'is_superuser': {
        'type': bool,
        'required': False
    },
    'password': {
        'type': str,
        'required': False
    },
}
