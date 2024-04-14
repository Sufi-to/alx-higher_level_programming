#!/usr/bin/python3
"""
adds a state with a city name using the relationship in sqlalchemy
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_add = State(name='California')
    city_add = City(name='San Francisco')
    state_add.cities.append(city_add)
    session.add(state_add)
    session.add(city_add)
    session.commit()
