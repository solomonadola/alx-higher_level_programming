#!/usr/bin/python3
"""
This module creates the State “California” with the
City “San Francisco” from the database hbtn_0e_100_usa.
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
    # Create a new State object with the name "California"
    new_state = State(name="California")
    # Append a new City object with the name
    # "San Francisco" to its cities attribute
    new_state.cities.append(City(name="San Francisco"))
    # Add the new State object to the database
    session.add(new_state)
    # Commit the changes
    session.commit()
    # Close the session
    session.close()
