from zope.interface import Interface
from zope.interface import implementer


class IManager(Interface):
    pass


@implementer(IManager)
class Manager(object):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def Tasks(self, param=None):
        pass

    def __configLoader(self):
        pass

    def __configWriter(self):
        pass
