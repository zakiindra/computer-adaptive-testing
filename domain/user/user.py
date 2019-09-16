from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, name, username, password, role, created, updated):
        self.id = id
        self.username = username
        self.name = name
        self.role = role
        self.password = password
        self.created = created
        self.updated = updated
