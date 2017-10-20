from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

Base = declarative_base()


class ToDo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    name = Column(String)


engine = create_engine('sqlite:///todo.sqlite')

session = Session(bind=engine)
Base.metadata.create_all(engine)
