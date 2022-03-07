#!/usr/bin/python3
'''Lists all city objects with each related state with just one query.'''

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

    for city in session.query(City).\
            options(joinedload(City.state)).\
            order_by(City.id).all():
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    session.close()
