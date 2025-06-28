from typing import List

from enums.Enums import ExpenseType
from models.User import UserModel


class SplitsModel:
    def __init__(self, user: UserModel, amount: int) -> None:
        self.user = user
        self.amount = amount


class ExpenseModel:
    def __init__(
        self,
        expense_id: str,
        paid_by: UserModel,
        amount: int,
        splits: List[SplitsModel],
        expense_type: ExpenseType,
    ) -> None:
        self.expense_id = expense_id
        self.paid_by = paid_by
        self.amount = amount
        self.splits = splits
        self.expense_type = expense_type
