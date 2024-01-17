#!/usr/bin/python3
"""
This module lists all City objects from a database.
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
    # Query the database and select the City and State objects
    for city in session.query(City).join(State).order_by(City.id):
        # Print the resu the format <city id>: <city name> -> <state name>
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    # Close the session
    session.close()
