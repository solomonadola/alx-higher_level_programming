#!/usr/bin/python3
"""
This module lists all State objects from a database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Create engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a session
    session = Session()
    # Query the database and print the results
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    # Close the session
    session.close()
