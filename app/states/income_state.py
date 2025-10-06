import reflex as rx
import datetime
from typing import TypedDict


class Income(TypedDict):
    id: int
    description: str
    amount: float
    date: str


class IncomeState(rx.State):
    incomes: list[Income] = [
        {"id": 1, "description": "Salary", "amount": 5000.0, "date": "2024-07-15"},
        {
            "id": 2,
            "description": "Freelance Project",
            "amount": 1200.0,
            "date": "2024-07-20",
        },
        {
            "id": 3,
            "description": "Stock Dividend",
            "amount": 300.0,
            "date": "2024-06-10",
        },
        {"id": 4, "description": "Salary", "amount": 5000.0, "date": "2024-06-15"},
    ]
    filter_year: str = str(datetime.date.today().year)
    filter_month: str = str(datetime.date.today().month).zfill(2)

    @rx.var
    def years(self) -> list[str]:
        all_years = {income["date"][:4] for income in self.incomes}
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
    def filtered_incomes(self) -> list[Income]:
        return [
            income
            for income in self.incomes
            if (self.filter_year == "" or income["date"].startswith(self.filter_year))
            and (self.filter_month == "" or income["date"][5:7] == self.filter_month)
        ]