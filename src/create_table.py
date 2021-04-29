from users.models import User


def create_tables():
    if not User.table_exists():
        print('creating users table')
        User.create_table()


if __name__ == '__main__':
    create_tables()
