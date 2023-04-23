#!/usr/bin/python3
"""this module deletes all State objects with a name containing the
letter a from the databasehbtn_0e_6_usa
script should take 3 arguments: mysql username, mysql password
and database name
must use the module SQLAlchemy
must import State and Base from model_state - from model_state
import Base, State
script should connect to a MySQL server running on localhost at port 3306
code should not be executed when imported"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


# create connection
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    # create all tables in the metadata
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # query
    state = session.query(State).all()
    for s in state:
        if 'a' in s.name:
            session.delete(s)
    session.commit()
    session.close()
