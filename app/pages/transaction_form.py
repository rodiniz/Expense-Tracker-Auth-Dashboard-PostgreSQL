import reflex as rx
from app.components.layout import layout
from app.states.transaction_form_state import TransactionFormState


def transaction_form():
    """A page for adding or editing an income or expense."""
    return layout(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    TransactionFormState.form_title,
                    class_name="text-2xl font-bold text-gray-800",
                ),
                class_name="mb-6",
            ),
            rx.el.div(
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Description", class_name="text-sm font-medium leading-none"
                        ),
                        rx.el.input(
                            placeholder="e.g. Salary, Groceries",
                            name="description",
                            default_value=TransactionFormState.description,
                            required=True,
                            class_name="flex h-9 w-full rounded-md border bg-transparent px-3 py-1 text-base shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 md:text-sm font-medium",
                        ),
                        class_name="flex flex-col gap-1.5",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Amount", class_name="text-sm font-medium leading-none"
                        ),
                        rx.el.input(
                            type="number",
                            placeholder="0.00",
                            name="amount",
                            default_value=TransactionFormState.amount,
                            required=True,
                            class_name="flex h-9 w-full rounded-md border bg-transparent px-3 py-1 text-base shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 md:text-sm font-medium",
                        ),
                        class_name="flex flex-col gap-1.5",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Date", class_name="text-sm font-medium leading-none"
                        ),
                        rx.el.input(
                            type="date",
                            name="date",
                            default_value=TransactionFormState.date,
                            required=True,
                            class_name="flex h-9 w-full rounded-md border bg-transparent px-3 py-1 text-base shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 md:text-sm font-medium",
                        ),
                        class_name="flex flex-col gap-1.5",
                    ),
                    rx.cond(
                        TransactionFormState.type == "expense",
                        rx.el.div(
                            rx.el.label(
                                "Group", class_name="text-sm font-medium leading-none"
                            ),
                            rx.el.select(
                                rx.foreach(
                                    TransactionFormState.all_groups,
                                    lambda group: rx.el.option(group, value=group),
                                ),
                                name="group",
                                default_value=TransactionFormState.group,
                                placeholder="Select a group",
                                required=True,
                                class_name="flex h-9 w-full rounded-md border bg-transparent px-3 py-1 text-base shadow-sm transition-colors focus-visible:outline-none focus-visible:ring-1 md:text-sm font-medium",
                            ),
                            class_name="flex flex-col gap-1.5",
                        ),
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            on_click=rx.redirect(
                                rx.cond(
                                    TransactionFormState.type == "income",
                                    "/incomes",
                                    "/expenses",
                                )
                            ),
                            type="button",
                            class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors text-gray-700 bg-gray-200 hover:bg-gray-300 h-9 px-4 py-2",
                        ),
                        rx.el.button(
                            "Save",
                            type="submit",
                            class_name="inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors text-white shadow bg-blue-500 hover:bg-blue-600 h-9 px-4 py-2",
                        ),
                        class_name="flex items-center gap-4 mt-6",
                    ),
                    on_submit=TransactionFormState.handle_submit,
                    class_name="flex flex-col gap-4",
                ),
                class_name="bg-white rounded-lg shadow-sm border border-gray-200 p-6 max-w-2xl",
            ),
        )
    )