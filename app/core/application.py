from zope.interface import Interface
from zope.interface import implementer


class IPictureManager(Interface):
    pass


@implementer(IPictureManager)
class PictureManager(object):
    def __init__(self):
        pass
