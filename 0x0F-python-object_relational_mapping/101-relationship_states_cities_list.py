#!/usr/bin/python3
"""
This module lists all State objects,
and corresponding City objects, from a database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
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
    # Query the database and join the State and City tables
    for state in session.query(State).join(City).order_by(State.id, City.id):
        # Print the state id and name
        print("{}: {}".format(state.id, state.name))
        # Print the city id and name with a tabulation
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    # Close the session
    session.close()
