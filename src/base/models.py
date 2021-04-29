from datetime import datetime

from peewee import Model, DateTimeField
from playhouse.postgres_ext import JSONField

from configs import db


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField()
    created_by = JSONField(default=dict)
    updated_by = JSONField(default=dict)

    class Meta:
        database = db
