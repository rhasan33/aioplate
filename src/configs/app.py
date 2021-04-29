import os

DEBUG = os.environ.get('DEBUG')
RABBITMQ_URL = os.environ.get('RABBITMQ_URL')
REDIS_HOST = os.environ.get('REDIS_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT', 5432)
DB_HOST = os.environ.get('DB_HOST', 'db')
APP_SALT = os.environ.get('APP_SALT')
AUTH_SERVICE = os.environ.get('AUTH_SERVICE')
