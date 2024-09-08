from textual.screen import Screen
from textual.widgets import Footer, Header, Label
from textual.app import ComposeResult


class ViewHabitsScreen(Screen):
    """The View Habits screen."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the View Habits screen."""

        yield Label("View Habits")
        yield Footer()
