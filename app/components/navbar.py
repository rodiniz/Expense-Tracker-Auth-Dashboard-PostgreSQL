import reflex as rx
from app.states.auth_state import AuthState


def navbar():
    """A navigation bar component for the top of the dashboard page."""
    return rx.el.header(
        rx.el.div(class_name="flex-1"),
        rx.el.div(
            rx.el.button(
                "Sign Out",
                on_click=AuthState.sign_out,
                class_name="bg-red-500 text-white px-3 py-1.5 rounded-md text-sm font-medium hover:bg-red-600 transition-colors",
            ),
            class_name="flex items-center gap-4",
        ),
        class_name="flex items-center justify-between w-full h-16 px-6 bg-white border-b border-gray-200",
    )