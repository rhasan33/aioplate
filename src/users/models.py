from peewee import CharField, BooleanField, Model
from playhouse.postgres_ext import ArrayField

from users.helpers import create_password, verify_password


class User(Model):
    username = CharField(max_length=150, unique=True)
    password = CharField(max_length=150)
    is_active = BooleanField(default=True)
    tags = ArrayField(field_class=CharField)
    name = CharField(max_length=150)
    email = CharField(max_length=200)

    class Meta:
        indexes = (
            ('email', True)
        )
        table_name = 'users'

    @staticmethod
    def set_password(raw_password: str) -> str:
        return create_password(raw_password=raw_password)

    def check_password(self, raw_password: str) -> bool:
        return verify_password(raw_password=raw_password, hash_pass=str(self.password))
