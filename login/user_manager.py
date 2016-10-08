from login import db
from models import User
from hashlib import sha256


class UserManager(object):
    @staticmethod
    def authenticate(username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.password == sha256(password).hexdigest():
            return True
        return False

    @staticmethod
    def user_exists(username):
        user = User.query.filter_by(username=username).first()
        if user:
            return True
        return False

    @staticmethod
    def add_user(username, password, email):
        try:
            password = sha256(password).hexdigest() # Encrypt password
            user = User(username=username, password=password, email=email)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            return False
        return True
