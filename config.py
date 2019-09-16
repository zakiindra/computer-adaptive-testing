import os


class Config:
    SECRET_KEY = os.getenv('CSRF_SECRET_KEY', 'yes-babe')
    MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE', 'cat')
    MYSQL_USER = os.getenv('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'root')
    DEFAULT_ADMIN_USER = os.getenv('DEFAULT_ADMIN_USER', 'admin')
    DEFAULT_ADMIN_PASSWORD = os.getenv('DEFAULT_ADMIN_PASSWORD', 'admin')
