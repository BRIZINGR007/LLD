from core.Singleton import SingletonMeta
from models.User import UserModel
from repositories.User import UserRepository


class UserService(metaclass=SingletonMeta):

    def __init__(self) -> None:
        self.user_repo = UserRepository()

    def add_user(self, user: UserModel) -> None:
        self.user_repo.add_user(user)

    def get_user(self, user_id) -> UserModel:
        return self.user_repo.get_user(user_id)
