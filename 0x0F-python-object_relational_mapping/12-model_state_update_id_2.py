#!/usr/bin/python3
"""this module changes the name of a State object from the database
hbtn_0e_6_usa
script should take 3 arguments: mysql username, mysql password
and database name
must use the module SQLAlchemy
must import State and Base from model_state - from model_state
import Base, State
script should connect to a MySQL server running on localhost at port 3306
Change the name of the State where id = 2 to New Mexico
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
    state_update = session.query(State).get(2)
    state_update.name = 'New Mexico'
    session.commit()
    session.close()
