import reflex as rx
from app.components.layout import layout


def groups():
    """Groups page."""
    return layout(rx.el.h1("Groups", class_name="text-2xl font-bold"))