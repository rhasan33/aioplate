from playhouse.postgres_ext import PostgresqlExtDatabase

from configs import DB_NAME, DB_USER, DB_PORT, DB_PASSWORD, DB_HOST

db = PostgresqlExtDatabase(
    database=DB_NAME,
    user=DB_USER,
    port=DB_PORT,
    password=DB_PASSWORD,
    host=DB_HOST,
    register_hstore=False,
)
