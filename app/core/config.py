from zope.interface import Interface
from zope.interface import implementer
from os.path import join
from os.path import exists
from os import getcwd

class IManager(Interface):
    pass

@implementer(IManager)
class Manager(object):
    def __init__(self):
        pass

    def __del__(self):
        pass

    def Tasks(self, param=None):
        if param == 'checkConfig':
            cfgFile = join(getcwd(), 'config.xml')
            if exists(cfgFile):
                return True
            else:
                return False

    def __configLoader(self):
        pass

    def __configWriter(self):
        pass
