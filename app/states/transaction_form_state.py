import reflex as rx
import datetime
from typing import Literal
import logging
from app.states.income_state import IncomeState, Income
from app.states.expense_state import ExpenseState, Expense


class TransactionFormState(rx.State):
    type: Literal["income", "expense"] = "income"
    transaction_id: int | None = None
    description: str = ""
    amount: str = ""
    date: str = str(datetime.date.today())
    group: str = ""

    @rx.var
    def form_title(self) -> str:
        action = "Edit" if self.transaction_id is not None else "Add"
        return f"{action} {self.type.capitalize()}"

    @rx.var
    async def all_groups(self) -> list[str]:
        expense_state = await self.get_state(ExpenseState)
        return sorted(list({expense["group"] for expense in expense_state.expenses}))

    @rx.event
    async def on_load(self):
        path_parts = self.router.page.path.strip("/").split("/")
        self.type = "income" if path_parts[0] == "incomes" else "expense"
        action = path_parts[1]
        if action == "edit":
            try:
                self.transaction_id = int(self.router.page.params.get("id"))
                await self._load_transaction_data()
            except (ValueError, TypeError) as e:
                logging.exception(f"Error loading transaction: {e}")
                return rx.redirect("/dashboard")
        else:
            self._reset_form()
            self.description = ""
            self.amount = ""
            self.date = str(datetime.date.today())
            self.group = ""

    async def _load_transaction_data(self):
        if self.type == "income":
            income_state = await self.get_state(IncomeState)
            transaction = next(
                (i for i in income_state.incomes if i["id"] == self.transaction_id),
                None,
            )
        else:
            expense_state = await self.get_state(ExpenseState)
            transaction = next(
                (e for e in expense_state.expenses if e["id"] == self.transaction_id),
                None,
            )
        if transaction:
            self.description = transaction["description"]
            self.amount = str(transaction["amount"])
            self.date = transaction["date"]
            if self.type == "expense":
                self.group = transaction.get("group", "")
        else:
            return rx.redirect(f"/{self.type}s")

    def _reset_form(self):
        self.transaction_id = None
        self.description = ""
        self.amount = ""
        self.date = str(datetime.date.today())
        self.group = ""

    @rx.event
    async def handle_submit(self, form_data: dict):
        self.description = form_data.get("description", "")
        self.amount = form_data.get("amount", "")
        self.date = form_data.get("date", datetime.date.today())
        if self.type == "expense":
            self.group = form_data.get("group", "")
        if self.type == "income":
            await self._save_income()
            return rx.redirect("/incomes")
        else:
            await self._save_expense()
            return rx.redirect("/expenses")

    async def _save_income(self):
        income_state = await self.get_state(IncomeState)
        try:
            amount_float = float(self.amount)
        except ValueError as e:
            logging.exception(f"Invalid amount for income: {e}")
            yield rx.toast("Invalid amount", duration=3000)
            return
        new_income = {
            "description": self.description,
            "amount": amount_float,
            "date": self.date,
        }
        if self.transaction_id is not None:
            new_income["id"] = self.transaction_id
            index = next(
                (
                    i
                    for i, inc in enumerate(income_state.incomes)
                    if inc["id"] == self.transaction_id
                ),
                -1,
            )
            if index != -1:
                income_state.incomes[index] = new_income
        else:
            new_id = (
                max((i["id"] for i in income_state.incomes)) + 1
                if income_state.incomes
                else 1
            )
            new_income["id"] = new_id
            income_state.incomes.append(new_income)

    async def _save_expense(self):
        expense_state = await self.get_state(ExpenseState)
        try:
            amount_float = float(self.amount)
        except ValueError as e:
            logging.exception(f"Invalid amount for expense: {e}")
            yield rx.toast("Invalid amount", duration=3000)
            return
        new_expense = {
            "description": self.description,
            "amount": amount_float,
            "date": self.date,
            "group": self.group,
        }
        if self.transaction_id is not None:
            new_expense["id"] = self.transaction_id
            index = next(
                (
                    i
                    for i, exp in enumerate(expense_state.expenses)
                    if exp["id"] == self.transaction_id
                ),
                -1,
            )
            if index != -1:
                expense_state.expenses[index] = new_expense
        else:
            new_id = (
                max((e["id"] for e in expense_state.expenses)) + 1
                if expense_state.expenses
                else 1
            )
            new_expense["id"] = new_id
            expense_state.expenses.append(new_expense)