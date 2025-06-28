from enums.Enums import ExpenseType
from models.User import UserModel
from services.Expense import ExpenseService
from services.User import UserService


def main():
    user_service: UserService = UserService()
    expense_service: ExpenseService = ExpenseService()
    user1 = UserModel(user_id="U_1", name="Killua", email="killua@gmail.com")
    user2 = UserModel(user_id="U_2", name="Gon", email="gon@gmail.com")
    user3 = UserModel(user_id="U_3", name="Naruto", email="gon@gmail.com")
    user4 = UserModel(user_id="U_4", name="Kakashi", email="gon@gmail.com")
    user_service.add_user(user1)
    user_service.add_user(user2)
    user_service.add_user(user3)
    user_service.add_user(user4)
    expense_service.add_expense(
        expense_id="E_1",
        paid_by=user_service.get_user("U_1"),
        amount=1000,
        users=[user_service.get_user("U_2"), user_service.get_user("U_4")],
        expense_type=ExpenseType.EQUAL,
    )
    amount_to_receive, amount_to_pay = expense_service.get_balance("U_1")
    print(
        f"Amount  to  Receive :  {amount_to_pay.items()} , Amount  to Pay  :  {amount_to_receive.items()}"
    )


if __name__ == "__main__":
    main()
