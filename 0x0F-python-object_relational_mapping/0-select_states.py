#!/usr/bin/python3
"""
This module lists all states from a database.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    This function connects to a MySQL server
    and lists all states from a database.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    """
    Main function that takes command line arguments
    and calls the function list_states.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
