from typing import Dict, List

from models.Expense import ExpenseModel


class ExpenseRepository:
    def __init__(self) -> None:
        self.expense: Dict[str, ExpenseModel] = dict()

    def add_expense(self, expense: ExpenseModel) -> None:
        self.expense[expense.expense_id] = expense

    def get_all_expenses(self) -> List[ExpenseModel]:
        return list(self.expense.values())
