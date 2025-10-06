import reflex as rx
from app.components.layout import layout


def dashboard():
    """The main dashboard page."""
    return layout(rx.el.h1("Dashboard", class_name="text-2xl font-bold"))