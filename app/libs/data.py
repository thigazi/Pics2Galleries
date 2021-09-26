from zope.interface import Interface, implementer
from platform import system

from ZODB import DB
from ZEO import ClientStorage
from os import getcwd


class IDBX(Interface):
    pass


@implementer(IDBX)
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
