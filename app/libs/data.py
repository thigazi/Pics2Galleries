from zope.interface import Interface, implementer
from platform import system

from ZODB import DB
from ZEO import ClientStorage
from os import getcwd
from sqlalchemy import create_engine
from .additional import Singleton

class IZODB(Interface):
    pass


@implementer(IZODB)
class DBX(object):

    def __init__(self):
        self.__fsx = ClientStorage.ClientStorage(getcwd() + '/dbx/zeosocket')

        self.__dbx = DB(self.__fsx)
        self.__conn = self.__dbx.open()
        self.root = self.__conn.root()

    def __delete__(self):
        self.__conn.close()
        self.__dbx.close()

        del self.root
        del self.__dbx
        del self.__conn
        del self.__fsx


class ISQLA(Interface):
    pass


@implementer(ISQLA)
class SQLA(Singleton):
    def __init__(self):
        print('here goes the config')
        '''
        self.engine = create_engine(
            '%s://%s:%s@%s:%s/%s' % (
                param['type'],
                param['user'],
                param['pass'],
                param['host'],
                param['port'],
                param['database'])
        )'''


class IMongoDB(Interface):
    pass


@implementer(IMongoDB)
class MongoDB(object):
    pass


class ICloudFileStorage(Interface):
    pass


@implementer(ICloudFileStorage)
class CloudFileStorage(object):
    def __init__(self):
        pass
