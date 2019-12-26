import os


def get_env(key, default_value=None):
    if key in os.environ:
        return os.environ[key]
    return default_value


MYSQL_USER = get_env('MYSQL_USER')
MYSQL_PASSWORD = get_env('MYSQL_PASSWORD')
MYSQL_HOST = get_env('MYSQL_HOST', 'db')
MYSQL_DATABASE = get_env('MYSQL_DATABASE')

SQLALCHEMY_DATABASE_URI = f'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}'
