from typing import Optional
from models.User import UserModel


class UserRepository:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, user: UserModel) -> None:
        self.users[user.user_id] = user

    def get_user(self, user_id: str) -> UserModel:
        user = self.users.get(user_id)
        if not user:
            raise Exception("No User Found fro teh following  Id")
        else:
            return user
