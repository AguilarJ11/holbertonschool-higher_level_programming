#!/usr/bin/python3
"""
script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":

    engine = create_engine(
        f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}",
        pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == sys.argv[4])
    states = states.order_by(State.id).all()
    if states:
        for state in states:
            print(state.id)
    else:
        print("Not found")
    session.close()
