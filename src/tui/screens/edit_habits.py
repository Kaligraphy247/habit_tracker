from textual.screen import Screen
from textual.widgets import Footer, Header, Label
from textual.app import ComposeResult


class EditHabitsScreen(Screen):
    """The Edit Habits screen."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the Edit Habits screen."""

        yield Label("Edit Habits")
        yield Footer()
