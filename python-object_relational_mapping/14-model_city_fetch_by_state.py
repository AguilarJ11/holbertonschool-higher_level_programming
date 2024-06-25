#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa:
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

    query = session.query(State, City).order_by(City.id).all()
    for s, c in query:
        print(f"{s.name}: {c.id} {c.name}")
    session.commit()
    session.close()
