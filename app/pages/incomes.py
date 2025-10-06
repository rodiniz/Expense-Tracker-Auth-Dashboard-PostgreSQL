import reflex as rx
from app.components.layout import layout
from app.states.income_state import IncomeState


def income_row(income: dict):
    """A row in the income table."""
    return rx.el.tr(
        rx.el.td(
            income["description"], class_name="px-4 py-3 font-medium text-gray-800"
        ),
        rx.el.td(f"${income['amount']:.2f}", class_name="px-4 py-3 text-gray-600"),
        rx.el.td(income["date"], class_name="px-4 py-3 text-gray-600"),
        rx.el.td(
            rx.el.div(
                rx.el.a(
                    rx.icon("pencil", class_name="h-4 w-4"),
                    href=f"/incomes/edit/{income['id']}",
                    class_name="text-blue-500 hover:text-blue-700",
                ),
                rx.el.button(
                    rx.icon("trash-2", class_name="h-4 w-4"),
                    class_name="text-red-500 hover:text-red-700",
                ),
                class_name="flex items-center justify-end gap-2",
            ),
            class_name="px-4 py-3 text-right",
        ),
        class_name="border-b border-gray-100 hover:bg-gray-50",
    )


def incomes():
    """Incomes page."""
    return layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1("Incomes", class_name="text-2xl font-bold text-gray-800"),
                rx.el.div(
                    rx.el.select(
                        rx.foreach(
                            IncomeState.months,
                            lambda month: rx.el.option(month[1], value=month[0]),
                        ),
                        on_change=IncomeState.set_filter_month,
                        value=IncomeState.filter_month,
                        class_name="px-3 py-1.5 border border-gray-300 rounded-md text-sm",
                    ),
                    rx.el.select(
                        rx.foreach(
                            IncomeState.years,
                            lambda year: rx.el.option(year, value=year),
                        ),
                        on_change=IncomeState.set_filter_year,
                        value=IncomeState.filter_year,
                        class_name="px-3 py-1.5 border border-gray-300 rounded-md text-sm",
                    ),
                    rx.el.a(
                        "New Income",
                        rx.icon("plus", class_name="h-4 w-4 ml-2"),
                        href="/incomes/add",
                        class_name="flex items-center bg-blue-500 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-600 transition-colors",
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex justify-between items-center mb-6",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Description",
                                class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th(
                                "Amount",
                                class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th(
                                "Date",
                                class_name="px-4 py-2 text-left text-sm font-semibold text-gray-600",
                            ),
                            rx.el.th(class_name="w-10"),
                        )
                    ),
                    rx.el.tbody(rx.foreach(IncomeState.filtered_incomes, income_row)),
                    class_name="w-full text-sm",
                ),
                class_name="bg-white rounded-lg shadow-sm border border-gray-200 overflow-hidden",
            ),
        )
    )