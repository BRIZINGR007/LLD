from collections import defaultdict
from typing import Dict, List, Optional, Tuple
from core.Singleton import SingletonMeta
from enums.Enums import ExpenseType
from models.Expense import ExpenseModel, SplitsModel
from models.User import UserModel
from repositories.Expense import ExpenseRepository
from repositories.User import UserRepository
from utils.ExpenseStrategyFactory import ExpenseStrategyFactory


class ExpenseService(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.user_repo = UserRepository()
        self.expense_repo = ExpenseRepository()

    def add_expense(
        self,
        expense_id: str,
        paid_by: UserModel,
        amount: int,
        users: List[UserModel],
        expense_type: ExpenseType,
        split_values: Optional[List[int]] = None,
    ) -> None:
        expense_strategy = ExpenseStrategyFactory.get_strategy(expense_type)
        splits = expense_strategy.split(
            users=users, amount=amount, split_values=split_values
        )
        expense = ExpenseModel(
            expense_id=expense_id,
            paid_by=paid_by,
            amount=amount,
            splits=splits,
            expense_type=expense_type,
        )
        self.expense_repo.add_expense(expense)

    def get_balance(self, user_id: str) -> Tuple[Dict[str, int], Dict[str, int]]:
        amount_to_recieve = defaultdict(int)
        amount_to_pay = defaultdict(int)
        expenses = self.expense_repo.get_all_expenses()
        for expense in expenses:
            paid_by = expense.paid_by.user_id
            if paid_by == user_id:
                for split in expense.splits:
                    amount_to_recieve[split.user.user_id] += split.amount
            else:
                for split in expense.splits:
                    if split.user.user_id == user_id:
                        amount_to_pay[paid_by] += split.amount
        return (amount_to_recieve, amount_to_pay)
