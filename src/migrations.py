from users.models import User

if not User.table_exists():
    User.create_table()
