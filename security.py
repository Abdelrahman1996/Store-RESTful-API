from werkzeug.security import safe_str_cmp
from models.user import UserModel
from passlib.apps import custom_app_context as pwd_context

def hash_password(password):
    self.password_hash = pwd_context.encrypt(password)

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and pwd_context.verify(hash_password(password),user.password_hash):
        return user

def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
