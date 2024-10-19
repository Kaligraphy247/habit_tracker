from typing import List
from src.models import User, Habit
from sqlmodel import Session, select
from sqlalchemy.orm import joinedload
from src.models.db import engine, create_db_and_tables


def get_users() -> List[User]:
    with Session(engine) as session:
        users = session.query(User).options(joinedload(User.habits)).all()
        return users

def save_habit(habit: Habit) -> bool:
    try:
        with Session(engine) as session:
            session.add(habit)
            session.commit()
            return True
    except Exception as e:
        print(e)
        return False