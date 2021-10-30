# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, String, Table, text
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class UserType(Base):
    __tablename__ = 'UserTypes'

    id = Column(INTEGER, primary_key=True, unique=True)
    Type = Column(String(45), nullable=False, unique=True)


class UserTable(Base):
    __tablename__ = 'UserTable'

    id = Column(INTEGER, primary_key=True, unique=True)
    utype = Column(ForeignKey('UserTypes.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    FirstName = Column(String(45), nullable=False)
    LastName = Column(String(45), nullable=False)
    EmailAddress = Column(String(45), nullable=False, unique=True)

    UserType = relationship('UserType')


class Session(UserTable):
    __tablename__ = 'sessions'

    id = Column(ForeignKey('UserTable.id'), primary_key=True)
    tlogin = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    sid = Column(String(60), nullable=False, unique=True)


t_Credentials = Table(
    'Credentials', metadata,
    Column('id', ForeignKey('UserTable.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True),
    Column('user', String(20), nullable=False, unique=True),
    Column('pass', String(45), nullable=False)
)
