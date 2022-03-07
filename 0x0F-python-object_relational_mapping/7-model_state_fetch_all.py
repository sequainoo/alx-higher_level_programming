#!/usr/bin/python3
'''Script returs State objects fro database'''

from re import I
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    conn_str = 'mysql+mysqldb://{:s}:{:s}@localhost:3306/{:s}'\
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(conn_str)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
