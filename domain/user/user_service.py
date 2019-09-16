from werkzeug.security import generate_password_hash, check_password_hash

from domain.user import role
from domain.user.role import Role
from domain.user.user import User


class UserService:

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create(self, user):
        if self.exists_by_name(user.username):
            return None
        user.password = self._generate_hash(user.password)
        return self.user_repository.create(user)

    def register_member_user(self, user_registration_form):
        user = self._to_user(user_registration_form)
        return self.create(user)

    def exists_by_name(self, username):
        return self.user_repository.exists_by_username(username)

    def get_user_by_username(self, username):
        return self.user_repository.read_by_username(username)

    def get_user_by_id(self, id):
        return self.user_repository.read_by_id(id)

    def get_all_member_users(self):
        return [user for user in self.user_repository.read_all() if user.role == Role.MEMBER]

    def check_password(self, username, plain_password):
        user = self.get_user_by_username(username)
        return check_password_hash(user.password, plain_password)

    def _generate_hash(self, plain_password):
        return generate_password_hash(plain_password)

    def _to_user(self, user_registration_form, id=None, role='member'):
        return User(id,
                    user_registration_form.name.data,
                    user_registration_form.username.data,
                    user_registration_form.password.data,
                    role,
                    None,
                    None)
