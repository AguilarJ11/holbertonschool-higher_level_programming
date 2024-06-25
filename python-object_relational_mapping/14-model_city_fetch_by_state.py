#!/usr/bin/python3
"""
script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from model_city import Base, City
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


