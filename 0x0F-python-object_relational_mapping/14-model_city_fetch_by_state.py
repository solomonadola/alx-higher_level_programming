#!/usr/bin/python3
"""
This module prints all City objects from a database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
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
    # Query the database and join the City and State tables
    t = session.query(City, State).join(State).order_by(City.id)
    for city, state in t:
        # Print the results in the format <state name>: (<city id>) <city name>
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    # Close the session
    session.close()
