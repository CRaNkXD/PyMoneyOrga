from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..account import Account


Base = declarative_base()
class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    acc_name = Column(String, nullable=False)
    balance = Column(Integer, nullable=False)


class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    acc_name = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    new_balance = Column(Integer, nullable=False)


class Database_sqlite():
    """description of class"""

    def __init__(self, file_name):
        engine = create_engine('sqlite:///' + file_name)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Sesession()


    def add_acc(self, acc_name, balance):
        """add an account to the the account table and commit to database"""
        self.session.add(Accounts(acc_name=acc_name,balance=balance))
        self.session.commit()


    def get_acc(self, acc_name):
        """get an account from the database"""
        acc = self.session.query(Accounts).filter_by(acc_name=acc_name).first() 
        return Account(acc_name, acc.balance)


    def update_acc_balance(self, acc_name, new_balance):
        """get an account from the database"""
        acc = self.session.query(Accounts).filter_by(acc_name=acc_name).first()
        acc.balance = new_balance
        self.session.commit()


    def add_transaction(self, acc_name, amount, new_balance):
        """add a transaction to the the transaction table and commit to database"""
        self.session.add(Transactions(acc_name=acc_name,amount=amount,new_balance=new_balance))
        self.session.commit()
