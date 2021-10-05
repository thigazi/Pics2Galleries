from .config import Manager, IManager
from zope.component import getGlobalSiteManager

gsx = getGlobalSiteManager()
gsx.registerUtility(Manager(), IManager)
