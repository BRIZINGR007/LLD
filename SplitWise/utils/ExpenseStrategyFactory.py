from typing import List
from enums.Enums import ExpenseType
from isp.strategy import BaseSplitStrategy
from models.Expense import SplitsModel
from models.User import UserModel


class EqualSplitStrategy(BaseSplitStrategy):
    def split(
        self, users: List[UserModel], amount: int, split_values: List[int] | None
    ) -> List[SplitsModel]:
        share = amount // len(users)
        return [SplitsModel(user=user, amount=share) for user in users]


class PercentSplitStrategy(BaseSplitStrategy):
    def split(
        self, users: List[UserModel], amount: int, split_values: List[int] | None
    ) -> List[SplitsModel]:
        if not split_values:
            raise Exception("split_values to be  provided for  Percent Split")
        return [
            SplitsModel(user=user, amount=int((per * amount) / 100))
            for user, per in zip(users, split_values)
        ]


class ExpenseStrategyFactory:
    @staticmethod
    def get_strategy(expense_type: ExpenseType) -> BaseSplitStrategy:
        match expense_type:
            case ExpenseType.EQUAL:
                return EqualSplitStrategy()
            case ExpenseType.PERCENT:
                return PercentSplitStrategy()
            case _:
                raise ValueError("Invalid Expense Type.")
