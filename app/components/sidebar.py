import reflex as rx


def sidebar_link(text: str, href: str, icon: str):
    """A link for the sidebar with an icon."""
    return rx.el.a(
        rx.icon(icon, class_name="h-5 w-5"),
        rx.el.span(text),
        href=href,
        class_name="flex items-center gap-3 rounded-lg px-3 py-2 text-gray-700 transition-all hover:bg-gray-200 font-medium",
    )


def sidebar():
    """The sidebar component for navigation."""
    return rx.el.div(
        rx.el.div(
            rx.el.a(
                rx.icon("wallet", class_name="h-6 w-6"),
                rx.el.span("Expense Tracker", class_name="text-lg font-semibold"),
                href="/dashboard",
                class_name="flex items-center gap-2 font-semibold",
            ),
            class_name="flex h-16 items-center border-b px-6",
        ),
        rx.el.nav(
            sidebar_link("Dashboard", "/dashboard", "layout-grid"),
            sidebar_link("Incomes", "/incomes", "trending-up"),
            sidebar_link("Expenses", "/expenses", "trending-down"),
            sidebar_link("Groups", "/groups", "package"),
            class_name="flex-1 flex flex-col gap-2 p-4",
        ),
        class_name="hidden border-r bg-gray-100/40 md:flex md:flex-col md:w-64",
    )