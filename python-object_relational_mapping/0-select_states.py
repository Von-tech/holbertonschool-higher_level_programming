#!/usr/bin/python3
"""
0-select_states module

This script connects to a MySQL database and retrieves all rows from
the `states` table, ordered by `id` in ascending order.
The script takes three command-line arguments: MySQL username,
MySQL password, and the database name.

Usage:
    ./0-select_states.py <username> <password> <database_name>
"""

import sys
import MySQLdb


def list_states(username, password, db_name):
    """
    Connects to the MySQL database and lists all states from the `states` table,
    sorted in ascending order by `id`.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the MySQL database.
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows in ascending order by `id`
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to list states
    list_states(username, password, db_name)

