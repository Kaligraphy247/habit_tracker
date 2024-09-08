from textual.screen import Screen
from textual.widgets import Footer, Header, Label
from textual.app import ComposeResult


class DeleteHabitsScreen(Screen):
    """The Delete Habits screen."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the Delete Habits screen."""

        yield Label("Delete Habits")
        yield Footer()
