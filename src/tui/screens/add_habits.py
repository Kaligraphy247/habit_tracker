from textual.screen import Screen
from textual.widgets import Footer, Header, Label, RichLog
from textual.widgets import Button, Input, RadioButton, RadioSet, Static, TextArea
from textual.app import ComposeResult
from textual.events import ScreenSuspend, ScreenResume, Event
from textual.widget import Widget
from textual.containers import Vertical, Horizontal
from textual.reactive import reactive
from src.models import Habit, utils
from textual import on, log
import datetime


class HabitsInput(Widget):
    def compose(self) -> ComposeResult:
        """Create child widgets for the Add Habits screen."""
        yield Label("Name")
        yield Input(placeholder="Name", id="name_input", valid_empty=False)
        yield Label("Description")
        yield TextArea(id="description_input")
        yield Label("Periodicity")
        with RadioSet(id="periodicity"):
            yield RadioButton("Weekly", id="weekly")
            yield RadioButton("Monthly", id="monthly")
        yield Button("Save", id="save_btn", variant="primary")

    @on(Input.Changed, selector="#name_input")
    def show_changed_name(self, event: Input.Changed) -> None:
        """Show the changed name in the log."""
        name_preview = self.parent.query_one("#name_preview", Static)
        name_preview.update(event.value)
        # set habit name
        new_habit = self.parent.new_habit
        new_habit.name = event.value

    @on(TextArea.Changed, selector="#description_input")
    def show_changed_description(self, event: TextArea.Changed) -> None:
        """Show the changed description in the log."""
        description_preview: TextArea = self.parent.query_one(
            "#description_preview", TextArea
        )
        description_preview.cursor_blink = False
        description_preview.load_text(event.control.text)  # set habit description
        new_habit = self.parent.new_habit
        new_habit.description = event.control.text

    @on(RadioSet.Changed, selector="#periodicity")
    def show_changed_periodicity(self, event: RadioSet.Changed) -> None:
        """Show the changed periodicity in the log."""
        print(self.parent)
        periodicity_preview = self.parent.query_one("#periodicity_preview", Static)
        periodicity_preview.update(event.pressed.label)
        # set habit periodicity
        new_habit = self.parent.new_habit
        new_habit.periodicity = str(event.pressed.label)

    @on(Button.Pressed, selector="#save_btn")
    def save_habit(self, event: Button.Pressed) -> None:
        """Save habit."""
        new_habit = self.parent.new_habit
        current_user = self.app.current_user
        if current_user is None:
            self.app.notify("Please select a user", title="Add Habit", severity="error")
            return

        new_habit.user_id = current_user.id
        new_habit.created_at = datetime.datetime.now()
        result = utils.save_habit(self.parent.new_habit)
        if not result:
            self.app.notify("Habit not saved", title="Add Habit", severity="error")
            return

        # Reset new habit
        self.parent.new_habit = Habit()
        self.app.notify("Habit saved", title="Add Habit", severity="information")


class HabitPreview(Widget):
    def compose(self) -> ComposeResult:
        """Create child widgets for the Add Habits screen."""
        yield Label("[bold]Preview", classes="title")

        # Name
        with Horizontal():
            yield Label("Name: ")
            yield Static(id="name_preview")

        # Description
        with Vertical():
            yield Label("Description: ")
            yield TextArea(id="description_preview", read_only=True)

        # Periodicity
        with Horizontal():
            yield Label("Periodicity: ")
            yield Static(id="periodicity_preview")


class AddHabitsScreen(Screen):
    """The Add Habits screen."""

    CSS_PATH = "styles/add_habits.tcss"

    new_habit: Habit = Habit()

    def __init__(self):
        super().__init__()

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
        elif event.key == "escape":
            self.app.switch_mode("welcome")
        else:
            print("Some other key pressed - Add Habits")
            print(event.key)

    def compose(self) -> ComposeResult:
        """Create child widgets for the Add Habits screen."""
        print(self.is_active)
        yield Label("Add Habits", classes="title")
        yield HabitsInput()
        yield HabitPreview()
        yield Footer()
