from sqlalchemy import Integer, Column, String, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True, nullable=False)
    currency_name = Column(String)
    datetime = Column(TIMESTAMP(timezone=True),
                      nullable=False, server_default=text('now()'))
    exchange_rate = Column(Integer)


class Users(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    datetime = Column(TIMESTAMP(timezone=True),
                      nullable=False, server_default=text('now()'))