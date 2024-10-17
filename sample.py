from src.models import User, Habit, Completions
from sqlmodel import Session, select
from src.models.db import engine, create_db_and_tables


if __name__ == "__main__":
    create_db_and_tables()

    def add_users():
        with Session(engine) as session:
            user1: User = User(name="John Doe", username="johndoe")
            user2: User = User(name="Jane Doe", username="janedoe")
            user3: User = User(name="Peter Griffin", username="pfin")

            session.add(user1)
            session.add(user2)
            session.add(user3)
            session.commit()


    def select_users():
        with Session(engine) as session:
            u1 = select(User).where(User.username == "johndoe")
            u2 = select(User).where(User.username == "janedoe")
            u3 = select(User).where(User.username == "pfin")
            users: User = session.exec(u1).all()
            print(users)
            # users = session.exec(u2).first()
            # print(users)
            # users = session.exec(u3).first()
            # print(users)
    
    # select_users()

    def add_habits():
        with Session(engine) as session:
            u1 = select(User).where(User.username == "johndoe")
            u1 = session.exec(u1).first()
            u2 = select(User).where(User.username == "janedoe")
            u2 = session.exec(u2).first()
            u3 = select(User).where(User.username == "pfin")
            u3 = session.exec(u3).first()

            # users: User = session.exec(u1).all()

            h1 = Habit(name="Running", periodicity="weekly", user_id=u1.id)
            h2 = Habit(name="Cycling", periodicity="weekly", user_id=u2.id)
            h3 = Habit(name="Swimming", periodicity="monthly", user_id=u3.id)
            h4 = Habit(name="Hiking", periodicity="weekly", user_id=u1.id)
            h5 = Habit(name="Climbing", periodicity="monthly", user_id=u2.id)

            session.add(h1)
            session.add(h2)
            session.add(h3)
            session.add(h4)
            session.add(h5)
            session.commit()

    # add_habits()

    def select_habits():
        with Session(engine) as session:
            h1 = select(Habit).where(Habit.name == "Running")
            h1 = session.exec(h1).all()
            print(h1)

            h2 = select(Habit).where(Habit.periodicity == "weekly")
            h2 = session.exec(h2).all()
            print(h2)

    # select_habits()

    def add_completions():
        with Session(engine) as session:
            h1 = select(Habit).where(Habit.name == "Running")
            h1 = session.exec(h1).first()
            h2 = select(Habit).where(Habit.name == "Cycling")
            h2 = session.exec(h2).first()
            h3 = select(Habit).where(Habit.name == "Swimming")
            h3 = session.exec(h3).first()

            c1 = Completions(habit_id=h1.id)
            c2 = Completions(habit_id=h2.id)
            c3 = Completions(habit_id=h3.id)

            session.add(c1)
            session.add(c2)
            session.add(c3)
            session.commit()

    # add_completions()


from src.utils import compare_datetimes
import datetime

strf_pattern = "%Y-%m-%d"
dt1 = datetime.datetime.now()
dt2 = dt1 + datetime.timedelta(days=4)
print(dt1.strftime(strf_pattern), dt2.strftime(strf_pattern))
# compare_datetimes()