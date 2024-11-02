#!/usr/bin/python3
"""
11-model_state_insert module

This script adds the State object "Louisiana" to the database hbtn_0e_6_usa.
The script takes three command-line arguments: MySQL username, MySQL password,
and the database name.

Usage:
    ./11-model_state_insert.py <username> <password> <database_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, db_name):
    """
    Adds the State object "Louisiana" to the given MySQL database
    and prints the new state's ID after creation.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Name of the MySQL database.
    """
    # Create the database engine
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    # Create all tables in the database (if they don’t exist)
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object for "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new state to the session and commit
    session.add(new_state)
    session.commit()

    # Print the new state's ID
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Call the function to add the state
    add_state(username, password, db_name)

