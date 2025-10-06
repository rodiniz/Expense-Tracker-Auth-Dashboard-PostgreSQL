import reflex as rx
from app.components.sidebar import sidebar
from app.components.navbar import navbar


def layout(*children: rx.Component) -> rx.Component:
    """The main layout for the dashboard pages."""
    return rx.el.div(
        sidebar(),
        rx.el.div(
            navbar(),
            rx.el.main(
                *children, class_name="flex-1 overflow-y-auto p-6 bg-gray-50/50"
            ),
            class_name="flex flex-col flex-1",
        ),
        class_name="flex min-h-screen w-full font-['Inter'] bg-gray-50/50",
    )