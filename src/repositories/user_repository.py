from database import db
from domain import User


class UserRepository:
    def add_user(self, user: User):
        db.users.insert_one(user.format_as_dict())

    def find_by_username(self, username: str) -> User:
        user = db.users.find_one({"username": username})
        return (
            User(
                username=user.get("username"),
                password=user.get("password"),
                name=user.get("name"),
            )
            if user
            else None
        )
