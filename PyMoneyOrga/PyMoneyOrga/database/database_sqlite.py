from sqlalchemy import create_engine
from sqlalchemy import (
    Integer,
    BigInteger,
    String,
    DateTime,
    ForeignKey,
    Column,
    MetaData,
    Table,
)
from sqlalchemy.orm import relationship, sessionmaker, mapper, clear_mappers
import datetime
from contextlib import contextmanager

from ..domain.account import Account, Transaction
from .database_interface import DatabaseInterface


class DatabaseSqlite(DatabaseInterface):
    """database implementation using sqlite3"""

    def __init__(self, url=None, file_name=None):
        self.file_name = file_name
        self.url = url
        # add try:
        if self.url is not None:
            engine = create_engine(url)
        elif self.file_name is not None:
            engine = create_engine("sqlite:///" + self.file_name)
        else:
            # add error
            pass
        self.meta_data = MetaData(bind=engine)
        self._define_and_map_tables(self.meta_data)
        self.meta_data.create_all()
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def _define_and_map_tables(self, meta_data):
        account = Table(
            "account",
            meta_data,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("_acc_name", String(50), nullable=False),
            Column("_balance", BigInteger, nullable=False),
        )

        transaction = Table(
            "transaction",
            meta_data,
            Column("id", Integer, primary_key=True, autoincrement=True),
            Column("account_id", ForeignKey("account.id", ondelete="CASCADE")),
            Column("amount", BigInteger, nullable=False),
            Column("new_balance", BigInteger, nullable=False),
            Column("time_stamp", DateTime, nullable=False),
            Column("description", String(50), nullable=False),
        )

        transaction_mapper = mapper(Transaction, transaction)
        mapper(
            Account,
            account,
            properties={
                "_transactions": relationship(
                    transaction_mapper,
                    cascade="all, delete, delete-orphan",
                    backref="account",
                )
            },
        )

    def _clear_all_tables(self):
        """
        close session delete all tables and clear mappers
        only used in unittest to tear down the tables
        """
        self.session.close()
        self.meta_data.drop_all()
        self.meta_data.create_all()
        clear_mappers()

    @contextmanager
    def get_session(self):
        """
        returns a session from the sessionmaker
        """
        session = self.Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def commit(self, session):
        """
        commits the changes done to the session into the db
        """
        session.commit()

    def expunge_all(self, session):
        """
        kepp access to all items after expiring
        """
        session.expunge_all()

    def close(self, session):
        """
        closes the session
        """
        session.close()

    def rollback(self, session):
        """
        rollback any changes in the session
        """
        session.rollback()

    def delete_acc(self, session, acc_name):
        acc = session.query(Account).filter_by(_acc_name=acc_name).first()
        if acc is None:
            return
        # you have to call the delete method on the session otherwise it is
        # called on the querry and the cascade options will not be used
        session.delete(acc)

    def get_all_acc(self, session):
        """
        returns a list of Account objects of all saved accounts
        from the database if none defined empty list []
        """
        accs = session.query(Account).all()
        return accs

    def add_acc(self, session, acc_name, balance):
        """add an account to the the account table and commit to database"""
        session.add(Account(acc_name=acc_name, balance=balance))

    def get_acc(self, session, acc_name) -> Account:
        """
        returns an Account object from the database.
        if not existing None
        """
        acc = session.query(Account).filter_by(_acc_name=acc_name).first()
        return acc
