import reflex as rx

USERS: dict[str, str] = {"admin@reflex.com": "password123"}


class AuthState(rx.State):
    is_logged_in: bool = True

    @rx.event
    def sign_up(self, form_data: dict):
        if form_data["email"] in USERS:
            yield rx.toast("Email already in use", duration=3000)
        else:
            USERS[form_data["email"]] = form_data["password"]
            self.is_logged_in = True
            return rx.redirect("/dashboard")

    @rx.event
    def sign_in(self, form_data: dict):
        if (
            form_data["email"] in USERS
            and USERS[form_data["email"]] == form_data["password"]
        ):
            self.is_logged_in = True
            return rx.redirect("/dashboard")
        else:
            self.is_logged_in = False
            yield rx.toast("Invalid email or password", duration=3000)

    @rx.event
    def sign_out(self):
        self.is_logged_in = False
        return rx.redirect("/sign-in")

    @rx.event
    def check_login(self):
        if not self.is_logged_in:
            return rx.redirect("/sign-in")