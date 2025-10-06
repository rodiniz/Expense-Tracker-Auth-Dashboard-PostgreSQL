import reflex as rx
from app.pages.sign_in import sign_in
from app.pages.sign_up import sign_up
from app.pages.dashboard import dashboard
from app.pages.incomes import incomes
from app.pages.expenses import expenses
from app.pages.groups import groups
from app.states.auth_state import AuthState

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(sign_in, route="/")
app.add_page(sign_in, route="/sign-in")
app.add_page(sign_up, route="/sign-up")
app.add_page(dashboard, route="/dashboard", on_load=AuthState.check_login)
app.add_page(incomes, route="/incomes", on_load=AuthState.check_login)
app.add_page(expenses, route="/expenses", on_load=AuthState.check_login)
app.add_page(groups, route="/groups", on_load=AuthState.check_login)
from app.pages.transaction_form import transaction_form
from app.states.transaction_form_state import TransactionFormState

app.add_page(
    transaction_form,
    route="/incomes/add",
    on_load=[AuthState.check_login, TransactionFormState.on_load],
)
app.add_page(
    transaction_form,
    route="/incomes/edit/[id]",
    on_load=[AuthState.check_login, TransactionFormState.on_load],
)
app.add_page(
    transaction_form,
    route="/expenses/add",
    on_load=[AuthState.check_login, TransactionFormState.on_load],
)
app.add_page(
    transaction_form,
    route="/expenses/edit/[id]",
    on_load=[AuthState.check_login, TransactionFormState.on_load],
)