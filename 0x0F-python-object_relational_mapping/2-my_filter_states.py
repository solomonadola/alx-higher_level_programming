#!/usr/bin/python3


"""
Lists all values in the states tables of a database where name
matches the argument
"""

import sys
import MySQLdb


def list_states(username, password, database, state_name):
    """
    This function connects to a MySQL server and lists all states from a
    database where the name matches the argument.
    It is safe from MySQL injections.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main function that takes command line arguments and calls the function
    list_states.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    list_states(username, password, database, state_name)
