from database.mongodb import db
from domain.user import User


class UserRepository:

    def find_by_username(self, username: str) -> User:
        user = db.users.find_one({"username": username})
        return User(username=user.get('username'), password=user.get('password'), name=user.get('name')) if user else None
