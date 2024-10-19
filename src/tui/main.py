from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.events import Key
from textual.widgets import Header, Footer, Button, Static, Label, RichLog
from src.tui.screens.view_habits import ViewHabitsScreen
from src.tui.screens.add_habits import AddHabitsScreen
from src.tui.screens.edit_habits import EditHabitsScreen
from src.tui.screens.delete_habits import DeleteHabitsScreen
from src.tui.screens.view_analytics import ViewAnalyticsScreen
# more
from src.models.db import engine, create_db_and_tables
from src.models import User
from src.models.utils import get_users
# 
from typing import List
from textual.reactive import reactive
from textual.widget import Widget
from textual.widgets import Collapsible, ListItem, ListView
from textual import on

# class User():


class TestScreen(Screen):
    go_back = ("escape", "app.pop_screen", "back")  # Pops Screen from Stack
    BINDINGS = [go_back, ("d", "toggle_dark", "Toggle dark mode - Test Screen V")]

    def compose(self) -> ComposeResult:

        yield Label("Test Screen")
        yield Footer()



class WelcomeScreen(Screen):
    """The welcome screen."""

    # BINDINGS = [
    #     ('h', "quit", "Quit"),
    # ]
    def compose(self) -> ComposeResult:
        """Create child widgets for the welcome screen."""

        ts = " " * 2  # Tab Space

        text = f"""\
        What would you like to do?\n
        {ts}1. View habits
        {ts}2. Add new habits
        {ts}3. Edit habits
        {ts}4. Delete habits
        {ts}5. View Analytics
        {ts}q. quit

        Press any key to continue ...
        Press b to get back to this screen.
        """
        yield Header(show_clock=True)
        yield UserWidget()
        yield Footer()
        yield Label("Habit Tracker", classes="welcome-title")
        yield Static(text, classes="welcome-text")

class UserWidget(Widget):
    def compose(self) -> ComposeResult:
        users: List[User] = self.app.users
        user_list_items = [ListItem(Label(user.name)) for user in users]
        """Create child widgets for the user screen."""
        with Collapsible(title="Select User"):
            yield Label(f"Current User: {self.app.current_user}", id="current_user_label")
            yield ListView(*user_list_items, id="user_list")
        
    @on(ListView.Selected, selector="#user_list")
    def select_user(self, event: ListView.Selected) -> None:
        user = self.app.users[event.control.index]
        current_user_label = self.query_one("#current_user_label", Label)
        current_user_label.update(f"Current User: {user.name}")
        self.app.current_user = user


class HabitTrackerApp(App):
    """A HabitTracker App with a TUI."""

    CSS_PATH = "main.tcss"
    TITLE = "HabitTracker"
    MODES = {
        "view_habits": ViewHabitsScreen,
        "add_habits": AddHabitsScreen,
        "edit_habits": EditHabitsScreen,
        "delete_habits": DeleteHabitsScreen,
        "view_analytics": ViewAnalyticsScreen,
        "test-screen": TestScreen,
        "welcome": WelcomeScreen,
    }
    # SCREENS = {"welcome": WelcomeScreen}
    SUB_TITLE = "A simple Habit Tracker"

    BINDINGS = [
        # ("d", "toggle_dark", "Toggle dark mode"),
        ("h", "switch_mode('welcome')", "🏠 Home"),
        ("1", "switch_mode('view_habits')", ""),
        ("2", "switch_mode('add_habits')", ""),
        ("3", "switch_mode('edit_habits')", ""),
        ("4", "switch_mode('delete_habits')", ""),
        ("5", "switch_mode('view_analytics')", ""),
        ("b", "switch_mode('welcome')", ""),
        ("q", "quit", "Quit"),
    ]

    current_user: reactive[User | None] = reactive(None)
    users: reactive[List[User] | None] = reactive(get_users())

    def on_mount(self) -> None:
        users = get_users()
        self.switch_mode("welcome")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit(self) -> None:
        """An action to quit the app."""
        print("Print this stuff before quitting")
        self.exit()

    def on_key(self, event: Key) -> None:
        """Handle key press events."""
        if event.key == "q":
            self.action_quit()
        else:
            print("Some other key pressed")
            print(event.key)


if __name__ == "__main__":
    create_db_and_tables()
    app = HabitTrackerApp()
    app.run()
