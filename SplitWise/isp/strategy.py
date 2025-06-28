from abc import ABC, abstractmethod
from typing import List, Optional

from models.Expense import SplitsModel
from models.User import UserModel


class BaseSplitStrategy(ABC):
    @abstractmethod
    def split(
        self, users: List[UserModel], amount: int, split_values: Optional[List[int]]
    ) -> List[SplitsModel]:
        raise NotImplementedError
