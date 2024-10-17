from typing import List
from textual.screen import Screen
from textual.widgets import Footer, Header, Label, Static
from textual.containers import ScrollableContainer
from textual.app import ComposeResult
from textual.geometry import Size
from rich.text import Text
from sqlmodel import Session, select
from sqlmodel import select, Session
from src.models import Habit, Completions
from src.models.db import engine


class ListHabitsView(Static):
    """List of Habits."""

    CSS = """
    ListHabitsView {
        height: 1fr;
        width: 100%;  /* Full width */
        border: solid 1px red;  /* Red solid border */
        padding: 1em;  /* Padding inside the border */
        margin: auto;  /* Center the whole widget */
        text-align: center;  /* Center the text inside */
    }

    Label {
        text-align: center;  /* Center the text in the label */
    }
    """

    def __init__(self):
        super().__init__()
        self.engine = engine
        self.habits = []

        with Session(engine) as session:
            habits = select(Habit).order_by(Habit.id)
            habits: List[Habit] = session.exec(habits).all()
            self.habits = habits

    def compose(self) -> ComposeResult:
        """Create child widgets for the View Habits screen."""

        # yield Container

        DEFAULT_CSS = """
            #title {
                text-style: bold;
            }
        """
        
        yield Label(f"{'':>4} {"Name":<15} {"Periodicity":<12} {"Streak":>5}", classes='title')

        for index, habit in enumerate(self.habits, 1):
            streak_display = "✔ " * habit.streak
            streak_display = streak_display[:10].ljust(10)
            period_display = f"({habit.periodicity})"

            yield Label(
                f"{index:>3}. {habit.name:<15} {period_display:<12} [{streak_display}]{habit.streak:>5}/{7 if habit.periodicity == "weekly" else 30}",
                classes="",
            )




class ViewHabitsScreen(Screen):
    """The View Habits screen."""

    # def get_content_width(self, container: Size, viewport: Size) -> int:
    #     """Get the content width."""
    #     return 80

    def compose(self) -> ComposeResult:
        """Create child widgets for the View Habits screen."""

        yield Label("View Habits", classes="welcome-title")
        # yield ScrollableContainer(ListHabitsView() )
        yield ListHabitsView()
        yield Footer()
