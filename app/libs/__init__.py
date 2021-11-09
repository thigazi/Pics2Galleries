from zope.component import getGlobalSiteManager
from zope.component.factory import Factory, IFactory
from .output import ITemplate, Template
from .data import DBX, SQLA

gsx = getGlobalSiteManager()
gsx.registerUtility(Template(), ITemplate)

DbxF = Factory(DBX, u'DbxF')
gsx.registerUtility(DbxF, IFactory, 'dbx')

SqlA = Factory(DBX, u'DbxF')
gsx.registerUtility(SqlA, IFactory, 'sqla')