from textual.screen import Screen
from textual.widgets import Footer, Header, Label
from textual.app import ComposeResult


class ViewAnalyticsScreen(Screen):
    """The View Analytics screen."""
    def on_mount(self) -> None:
        print("Mounted View Analytics Screen")
        print(self, self.app)


    def compose(self) -> ComposeResult:
        """Create child widgets for the View Analytics screen."""

        yield Label("View Analytics")
        yield Footer()
