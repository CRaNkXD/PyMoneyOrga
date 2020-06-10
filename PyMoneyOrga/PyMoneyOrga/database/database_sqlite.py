from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import select
from sqlalchemy.ext.declarative import declarative_base
from .database import Database

Base = declarative_base()
class Account(Base):
    __tablename__ = "account"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    balance = Column(Integer, nullable=False)

class Transaction(Base):
    __tablename__ = "trasaction"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    new_balance = Column(Integer, nullable=False)

class Database_sqlite(Database):
    """description of class"""

    def __init__(self, file_name):
        super().self.__init__(self, file_name)

        engine = create_engine('sqlite:///pymoneyorga.sqlite')
        # connection = engine.connect()
        meta = MetaData(engine)
        Table_pymoneyorga = Table('Table_pymoneyorga', meta,
           Column('id', Integer, primary_key=True),
           Column('name',String),
           Column('cash',Integer),
           )
