#!/usr/bin/python3
"""
This module lists all cities from a database
where the state name matches the argument.
"""

import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """
    This function connects to a MySQL server and lists all cities from a
    database where the state name matches the argument.
    It is safe from MySQL injections.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT cities.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main function that takes command line arguments and calls the function
    list_cities.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    list_cities(username, password, database, state_name)
