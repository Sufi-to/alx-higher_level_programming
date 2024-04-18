#!/usr/bin/python3
"""
Lists all state objects and their cities in the db
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
    obj_list = session.query(State).order_by(State.id)
    for instance in obj_list:
        print(f"{instance.id}: {instance.name}")
        for c_obj in instance.cities:
            print("    ", end="")
            print(f"{c_obj.id}: {c_obj.name}")

