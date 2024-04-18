#!/usr/bin/python3
"""
Contains a state class that inherits from Base class that is an
intance of declarative base and a relationship with the cities table
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


this_metadata = MetaData()
Base = declarative_base(metadata=this_metadata)


class State(Base):
    """ This is a state class """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='states', cascade='all, delete")
