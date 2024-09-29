# Represents Classes/Objects

from sqlmodel import SQLModel, Field, DateTime, Relationship
from typing import List, Optional
import datetime

class Completions(SQLModel, table=True):
    """
    Class for Completions. Represents a single habit completion.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    habit_id: int = Field(foreign_key="habit.id", nullable=False)
    completion_date: datetime.datetime = Field(
        default_factory=datetime.datetime.now, nullable=False
    )
    
    # Set relationship back to Habit
    habit: "Habit" = Relationship(back_populates="completions")

    def __repr__(self):
        return f"<Completion id={self.id} habit_id={self.habit_id} date={self.completion_date}>"


class Habit(SQLModel, table=True):
    """
    Class for Habit. Represents a single Habit.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None, nullable=False)
    description: Optional[str] = Field(default="", nullable=True)
    periodicity: str = Field(default="weekly", nullable=False) # weekly | monthly
    streak: int = Field(default=0, nullable=False)
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now, nullable=False
    )
    user_id: int = Field(foreign_key="user.id", nullable=False)

    # Relationship to User model
    user: "User" = Relationship(back_populates="habits")
    
    # Relationship to Completion model
    completions: List["Completions"] = Relationship(
        back_populates="habit",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )

    def __repr__(self):
        return f"<Habit id={self.id}, name={self.name}, streak={self.streak}>"


class User(SQLModel, table=True):
    """
    Class for User. Represents a User.
    """

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default=None, nullable=False)
    username: str = Field(default=None, nullable=False)
    created_at: datetime.datetime = Field(
        default_factory=datetime.datetime.now, nullable=False
    )

    # Relationship to the Habit model
    habits: List["Habit"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"cascade": "all, delete, delete-orphan"},
    )

    def __repr__(self):
        return f"<User id={self.id} name={self.name} habits='{len(self.habits)}'>"

    def list_habits(self):
        return self.habits



# class Analytics:
#     """
#         Class for Analytics.
#         This is a Service Class and does not need to be a model/table.
#     """
#     def __init__(self, user: User):
#         self.user = user
