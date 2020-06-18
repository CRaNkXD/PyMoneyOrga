from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, BigInteger, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime

from .database_interface import Database_interface


Base = declarative_base()
class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    acc_name = Column(String, nullable=False)
    balance = Column(BigInteger, nullable=False)

    transactions = relationship("Transactions", back_populates="account", cascade="all, delete-orphan")


class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    amount = Column(BigInteger, nullable=False)
    new_balance = Column(BigInteger, nullable=False)
    time_stamp = Column(DateTime, nullable=False)

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


    def _clear_all_tables(self):
        session = self.Session()
        engine = session.get_bind()
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)


    def get_all_acc(self):
        """returns a dictionary {acc_name:balance} of all saved accounts from the database"""
        accs_dict = {}
        session = self.Session()
        accs = session.query(Accounts).all()
        if accs is None:
            session.close()
            return {}

        for acc in accs:
            accs_dict[acc.acc_name] = acc.balance

        session.close()
        return accs_dict


    def get_all_transaction(self, acc_name):
        """returns a list [transactions] of all trnsactions for specified account from the database"""
        transactions = []
        session = self.Session()
        acc = session.query(Accounts).filter_by(acc_name=acc_name).first()
        if acc is None:
            return []

        transactions = acc.transactions
        session.close()
        return transactions


    def get_transaction(self, acc_name, time_stamp):
        """returns a transaction from the database"""
        transactions = []
        session = self.Session()
        acc = session.query(Accounts).filter_by(acc_name=acc_name).first()
        if acc is None:
            session.close()
            return None

        for transaction in acc.transactions:
            if transaction.time_stamp == time_stamp:
                session.close()
                return transaction
        
        return None


    def add_acc(self, acc_name, balance):
        """add an account to the the account table and commit to database"""
        session = self.Session()
        session.add(Accounts(acc_name=acc_name,balance=balance))
        session.commit()
        session.close()


    def get_acc(self, acc_name):
        """returns a dictionary {acc_name:balance} from the database. if not existing {acc_name:None}"""
        session = self.Session()
        acc = session.query(Accounts).filter_by(acc_name=acc_name).first()
        session.close()
        if acc is None:
            session.close()
            return {acc_name: None}
        return {acc.acc_name: acc.balance}


    def update_acc_balance(self, acc_name, new_balance):
        """get an account from the database"""
        session = self.Session()
        acc = session.query(Accounts).filter_by(acc_name=acc_name).first()
        if acc is None:
            session.close()
            # raise exception
        else:
            acc.balance = new_balance
            session.commit()
            session.close()


    def add_transaction(self, acc_name, amount, new_balance):
        """add a transaction to the transaction table and commit to database return the time stamp used to save the tran"""
        session = self.Session()
        acc = session.query(Accounts).filter_by(acc_name=acc_name).first() 
        if acc is None:
            session.close()
            # raise exception
            return None
        else:
            time_stamp = datetime.datetime.now()
            session.add(Transactions(account_id=acc.id, amount=amount, new_balance=new_balance, time_stamp=time_stamp ))
            session.commit()
            session.close()
            return time_stamp