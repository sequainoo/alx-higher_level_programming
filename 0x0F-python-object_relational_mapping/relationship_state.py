#!/usr/bin/python3
'''State definition'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
# from relationship_city import City

Base = declarative_base()


class State(Base):
    '''State model.'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                          back_populates='state',
                          cascade='all, delete, delete-orphan')
