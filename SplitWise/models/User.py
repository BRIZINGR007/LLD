from typing import Optional


class UserModel:
    def __init__(self, user_id: str, name: str, email: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email

