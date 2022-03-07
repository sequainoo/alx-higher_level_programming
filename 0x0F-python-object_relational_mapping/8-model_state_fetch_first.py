#!/usr/bin/python3
'''Prints the first State Object fro database'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(conn_str,  pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).first()
    if first_state:
        print('{:d}: {:s}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')
    session.close()
