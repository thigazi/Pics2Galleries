from .config import Manager, IManager
from .application import IPictureManager,PictureManager

from zope.component import getGlobalSiteManager

gsx = getGlobalSiteManager()
gsx.registerUtility(Manager(), IManager)
gsx.registerUtility(PictureManager(), IPictureManager)
