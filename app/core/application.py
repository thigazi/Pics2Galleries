from zope.interface import Interface
from zope.interface import implementer


class ISessionHandler(Interface):
    pass


@implementer(ISessionHandler)
class SessionHandler(object):
    def __init__(self):
        pass


class IPictureManager(Interface):
    pass


@implementer(IPictureManager)
class PictureManager(object):
    def __init__(self):
        pass
