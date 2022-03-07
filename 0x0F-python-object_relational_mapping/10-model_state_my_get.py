#!/usr/bin/python3
'''script that prints the State object with the name passed as argument'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

if __name__ == '__main__':
    conn_str = 'mysql+mysqldb://{:s}:{:s}@localhost:3306/{:s}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(conn_str,  pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter(State.name == sys.argv[4])\
            .one()
        print(state.id)
    except (NoResultFound, MultipleResultsFound):
        print('Not Found')

    session.close()
