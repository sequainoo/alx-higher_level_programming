#!/usr/bin/python3
'''Script creates a State with an associated city using relationship'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
    )
    engine = create_engine(conn_str, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # Base.metadata.create_all(engine)

    for state in session.query(State).\
            order_by(State.id).all():
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()
