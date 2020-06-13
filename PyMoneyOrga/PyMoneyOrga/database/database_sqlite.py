from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .database_interface import Database_interface


Base = declarative_base()
class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    acc_name = Column(String, nullable=False)
    balance = Column(Integer, nullable=False)

    transactions = relationship("Transactions", back_populates="account", cascade="all, delete-orphan")


class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(Integer, nullable=False)
    new_balance = Column(Integer, nullable=False)

    account = relationship("Accounts", back_populates="transactions")


class Database_sqlite(Database_interface):
    """database implementation using sqlite3"""

    def __init__(self, url = None, file_name = None):
        self.file_name = file_name
        self.url = url
        # add try:
        if self.url != None:
            engine = create_engine(url)
        elif self.file_name != None:
            engine = create_engine('sqlite:///' + self.file_name)

        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)


    def get_all_acc(self):
        """returns a dictionary {acc_name:balance} of all saved accounts from the database"""
        accs_dict = {}
        session = self.Session()
        accs = session.query(Accounts).all()
        for acc in accs:
            accs_dict[acc.acc_name] = acc.balance

        session.close()
        return accs_dict

    def add_acc(self, acc_name, balance):
        """add an account to the the account table and commit to database"""
        session = self.Session()
        session.add(Accounts(acc_name=acc_name,balance=balance))
        session.commit()
        session.close()


    def get_acc(self, acc_name):
        """get an account from the database"""
        session = self.Session()
        acc = session.query(Accounts).filter_by(acc_name=acc_name).first() 
        session.close()
        return {acc.acc_name: acc.balance}


    def update_acc_balance(self, acc_name, new_balance):
        """get an account from the database"""
        session = self.Session()
        acc = session.query(Accounts).filter_by(acc_name=acc_name).first()
        acc.balance = new_balance
        session.commit()
        session.close()


    def add_transaction(self, acc_name, amount, new_balance):
        """add a transaction to the the transaction table and commit to database"""
        session = self.Session()
        session.add(Transactions(acc_name=acc_name,amount=amount,new_balance=new_balance))
        session.commit()
        session.close()
