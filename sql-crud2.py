from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
# we're using the postres server on our local server in order to connect to our chinook database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Famous Landmarks" table
class FamousLandmarks(base):
    __tablename__ = "Famous Places"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    city = Column(String)
    year_built = Column(Integer)
    height = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()


# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our FamousLandmarks table
eiffel_tower = FamousLandmarks(
    country = "France",
    city = "Paris",
    year_built = 1889,
    height = 324,
)

statue_of_liberty = FamousLandmarks(
    country = "USA",
    city = "New York",
    year_built = 1884,
    height = 92,
)

leaning_tower = FamousLandmarks(
    country = "Italy",
    city = "Pisa",
    year_built = 1399,
    height = 60,
)


# add each instance of our landmarks to our session
# session.add(eiffel_tower)
# session.add(statue_of_liberty)
# session.add(leaning_tower)


# delete multiple records if duplicated while creating

landmarks = session.query(FamousLandmarks)
for landmark in landmarks:
    if landmark.id > 3:
        session.delete(landmark)

    session.commit()

# query the database to find all Landmarks
landmarks = session.query(FamousLandmarks)
for landmark in landmarks:
    print(
        landmark.id,
        landmark.country,
        landmark.city,
        landmark.year_built,
        landmark.height,
        sep=" | "
    )