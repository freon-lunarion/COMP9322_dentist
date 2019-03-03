from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from sqlalchemy import Column, Integer, String
from sqlalchemy import PickleType

import uuid


Base = declarative_base()
engine = create_engine('sqlite:///:memory:', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base.query = db_session.query_property()

def init_db():
   # create tables
   Base.metadata.create_all(bind=engine)

class Timeslot(Base):
    __tablename__ = 'timeslot'
    id = Column(String, primary_key=True)
    day = Column(String)
    start = Column(String)
    end = Column(String)
    def __init__(self, day, start, end):
       super().__init__()
       self.id = uuid.uuid4
       self.day = day
       self.start = start
       self.end = end
