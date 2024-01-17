#!/usr/bin/python3
"""
This module lists all cities from a database.
"""

import MySQLdb
import sys


def list_cities(username, password, database):
    """
    This function connects to a MySQL server and lists all cities from a
    database.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             INNER JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
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
    list_cities(username, password, database)
