from textual.screen import Screen
from textual.widgets import Footer, Header, Label
from textual.app import ComposeResult
from textual.events import ScreenSuspend, ScreenResume, Event

class AddHabitsScreen(Screen):
    """The Add Habits screen."""

    def on_mount(self) -> None:
        print(self)
        print("Mounted Add Habits Screen")

    def on_screen_resume(self, event: ScreenResume) -> None:
        print("Resumed Add Habits Screen")
        print(self)

    def on_screen_suspend(self, event: ScreenSuspend) -> None:
        print("Suspended Add Habits Screen")
        print(self.is_active)

    def on_key(self, event: Event) -> None:
        """Handle key press events."""
        print("Screen ID: ", self.screen.name)
        if event.key == "q":
            self.app.action_quit()
        else:
            print("Some other key pressed - Add Habits")
            print(event.key)

    def compose(self) -> ComposeResult:
        """Create child widgets for the Add Habits screen."""
        print(self.is_active)
        yield Label("Add Habits")
        yield Footer()
