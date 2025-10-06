import reflex as rx
import datetime
from typing import TypedDict


class Expense(TypedDict):
    id: int
    description: str
    amount: float
    date: str
    group: str


class ExpenseState(rx.State):
    expenses: list[Expense] = [
        {
            "id": 1,
            "description": "Groceries",
            "amount": 150.75,
            "date": "2024-07-10",
            "group": "Food",
        },
        {
            "id": 2,
            "description": "Electricity Bill",
            "amount": 75.5,
            "date": "2024-07-12",
            "group": "Utilities",
        },
        {
            "id": 3,
            "description": "Gas",
            "amount": 50.0,
            "date": "2024-07-18",
            "group": "Transport",
        },
        {
            "id": 4,
            "description": "Rent",
            "amount": 1200.0,
            "date": "2024-07-01",
            "group": "Housing",
        },
        {
            "id": 5,
            "description": "Dinner out",
            "amount": 80.2,
            "date": "2024-06-25",
            "group": "Food",
        },
    ]
    filter_year: str = str(datetime.date.today().year)
    filter_month: str = str(datetime.date.today().month).zfill(2)

    @rx.var
    def years(self) -> list[str]:
        all_years = {expense["date"][:4] for expense in self.expenses}
        return sorted(list(all_years), reverse=True)

    @rx.var
    def months(self) -> list[tuple[str, str]]:
        return [
            ("01", "January"),
            ("02", "February"),
            ("03", "March"),
            ("04", "April"),
            ("05", "May"),
            ("06", "June"),
            ("07", "July"),
            ("08", "August"),
            ("09", "September"),
            ("10", "October"),
            ("11", "November"),
            ("12", "December"),
        ]

    @rx.var
    def filtered_expenses(self) -> list[Expense]:
        return [
            expense
            for expense in self.expenses
            if (self.filter_year == "" or expense["date"].startswith(self.filter_year))
            and (self.filter_month == "" or expense["date"][5:7] == self.filter_month)
        ]