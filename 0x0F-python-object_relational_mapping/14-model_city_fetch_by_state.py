#!/usr/bin/python3
'''Script gets cities with their states'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
    )
    engine = create_engine(conn_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City).\
        join(State, City.state_id == State.id).\
        order_by(City.id).all()

    for row in results:
        print('{:s}: ({:d}) {:s}'.format(row.state.name, row.id, row.name))
