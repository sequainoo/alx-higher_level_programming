#!/usr/bin/python3
'''script that adds the State object “Louisiana” to the database'''

import sys
from sqlalchemy import delete
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    conn_str = 'mysql+mysqldb://{:s}:{:s}@localhost:3306/{:s}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(conn_str,  pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name='Louisiana')

    session.add(louisiana)
    session.flush()
    session.commit()
    print(louisiana.id)
    session.close()
