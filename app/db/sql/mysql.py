# coding: utf-8
from sqlalchemy import CHAR, Column, DateTime, ForeignKey, LargeBinary, String, Table
from sqlalchemy.dialects.mysql import INTEGER, MEDIUMTEXT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class GalleryAlbum(Base):
    __tablename__ = 'GalleryAlbum'

    id = Column(INTEGER, primary_key=True, unique=True)
    AlbumTitle = Column(String(40), nullable=False)
    AlbumDescription = Column(MEDIUMTEXT, nullable=False)
    PictureSizeSettings = Column(String(45))


class GalleryAlbumSetting(GalleryAlbum):
    __tablename__ = 'GalleryAlbumSettings'

    id = Column(ForeignKey('GalleryAlbum.id'), primary_key=True)
    PictureWidth = Column(INTEGER, nullable=False)
    PictureHeight = Column(INTEGER, nullable=False)


t_GetNames = Table(
    'GetNames', metadata,
    Column('First Name', String(45)),
    Column('Last Name', String(45))
)


class UserType(Base):
    __tablename__ = 'UserTypes'

    id = Column(INTEGER, primary_key=True, unique=True)
    Type = Column(String(45), nullable=False, unique=True)


class GalleryItem(Base):
    __tablename__ = 'GalleryItems'

    id = Column(INTEGER, primary_key=True, unique=True)
    AlbumId = Column(ForeignKey('GalleryAlbum.id'), nullable=False, index=True)
    thumbnail = Column(LargeBinary)
    Rawpicture = Column(String(45))
    ExtensionType = Column(CHAR(3))

    GalleryAlbum = relationship('GalleryAlbum')


class UserTable(Base):
    __tablename__ = 'UserTable'

    id = Column(INTEGER, primary_key=True, unique=True)
    utype = Column(ForeignKey('UserTypes.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    FirstName = Column(String(45), nullable=False)
    LastName = Column(String(45), nullable=False)
    EmailAddress = Column(String(45), nullable=False, unique=True)

    UserType = relationship('UserType')


class GalleryAcces(UserTable):
    __tablename__ = 'GalleryAccess'

    id = Column(ForeignKey('UserTable.id'), primary_key=True)
    AlbumId = Column(ForeignKey('GalleryAlbum.id'), nullable=False, index=True)
    Role = Column(String(20))

    GalleryAlbum = relationship('GalleryAlbum')


class Session(UserTable):
    __tablename__ = 'sessions'

    id = Column(ForeignKey('UserTable.id'), primary_key=True)
    tlogin = Column(DateTime)
    sid = Column(String(60), nullable=False, unique=True)


class Credential(Base):
    __tablename__ = 'Credentials'

    id = Column(INTEGER, primary_key=True, unique=True)
    cid = Column(ForeignKey('UserTable.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    user = Column(String(20), nullable=False, unique=True)
    _pass = Column('pass', String(45), nullable=False)

    UserTable = relationship('UserTable')


class RawItem(Base):
    __tablename__ = 'RawItem'

    id = Column(INTEGER, primary_key=True, unique=True)
    gid = Column(ForeignKey('GalleryItems.id'), nullable=False, index=True)
    Rawpicture = Column(LargeBinary, nullable=False)

    GalleryItem = relationship('GalleryItem')
