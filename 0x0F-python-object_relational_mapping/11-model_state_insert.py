#!/usr/bin/python3
"""this module adds the State object “Louisiana” to the database
hbtn_0e_6_usa
script should take 3 arguments: mysql username, mysql password
and database name
must use the module SQLAlchemy
must import State and Base from model_state - from model_state
import Base, State
script should connect to a MySQL server running on localhost at port 3306
Print the new states.id after creation
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

    # add new state object
    new_obj = State(name='Louisiana')

    session.add(new_obj)
    session.commit()

    # query
    state = session.query(State).filter_by(name='Louisiana').first()
    if state is not None:
        print('{}'.format(state.id))
    else:
        print('Not Found')
    session.close()
