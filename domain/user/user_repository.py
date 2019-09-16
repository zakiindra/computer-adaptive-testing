import mysql.connector as mysql

from domain.user.user import User


class UserRepository:

    def __init__(self, config):
        self.db = mysql.connect(
            host=config.MYSQL_HOST,
            database=config.MYSQL_DATABASE,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD
        )
        self.db.autocommit = True

    def exists_by_username(self, username):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM user WHERE username = '%s'" % username)
        cursor.fetchall()
        exists = cursor.rowcount > 0
        cursor.close()
        return exists

    def read_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM user WHERE id = '%s'" % id)
        row = cursor.fetchone()
        cursor.close()
        return self._row_to_user(row)

    def read_by_username(self, username):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM user WHERE username = '%s'" % username)
        row = cursor.fetchone()
        cursor.close()
        return self._row_to_user(row)

    def create(self, user):
        print('Creating new user: ({}, {}, {}, {})'.format(user.name, user.username, user.password, user.role))
        cursor = self.db.cursor()
        cursor.execute("""
        INSERT INTO user(name, username,  password, role)
        VALUE (%s, %s, %s, %s)
        """, (user.name, user.username, user.password, user.role))
        cursor.close()
        return user

    def read_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM user ORDER BY created")
        rows = cursor.fetchall()
        users = []
        for row in rows:
            users.append(self._row_to_user(row))
        return users

    def _row_to_user(self, row):
        print(row)
        return User(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
