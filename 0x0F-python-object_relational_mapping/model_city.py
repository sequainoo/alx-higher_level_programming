#!/usr/bin/python3
'''State definition'''

from model_state import Base, State
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    '''Model of a City.'''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship(State, back_populates='cities')


State.cities = relationship(City, back_populates='state')
