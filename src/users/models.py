from datetime import datetime

from playhouse.postgres_ext import *
from configs import db


class User(Model):
    GENDER = (
        ('male', 'Male'),
        ('female', 'female'),
    )

    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    gender = CharField(max_length=10, choices=GENDER, default='male')
    username = CharField(max_length=40, unique=True)
    date_joined = DateTimeField(default=datetime.now)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)
    is_superuser = BooleanField(default=False)
    password = CharField(max_length=150)

    class Meta:
        database = db
        db_table = 'users'
        indexes = (
            (('first_name', 'last_name', 'user_status'), True),
        )
