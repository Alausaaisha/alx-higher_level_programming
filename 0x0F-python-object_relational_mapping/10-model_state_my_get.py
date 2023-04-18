#!/usr/bin/python3
"""This module prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
Your script should take 4 arguments: mysql username, mysql password,
database name and state name to search (SQL injection free)
You must use the module SQLAlchemy
You must import State and Base from model_state - from model_state
import Base, State
Your script should connect to a MySQL server running on localhost
at port 3306
You can assume you have one record with the state name to search
Results must display the states.id
If no state has the name you searched for, display Not found
Your code should not be executed when imported"""


import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all tables stored in this metadata
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    if len(sys.argv) == 5:
        search_result = sys.argv[4]
        result = session.query(State).filter_by(name=search_result).first()
        if result is not None:
            print("{}".format(result.id))
        else:
            print("Not found")
    session.close()
