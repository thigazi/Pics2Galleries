from zope.interface import Interface
from zope.interface import implementer
from re import search as re_search
from os.path import exists


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

    def Tasks(self, app, params):
        rset = None
        if app == 'verifyInput':
            rset = self.__verifyInput(params)

        return rset

    def __verifyInput(self, param):
        result = None
        if param['section'] == 'Initialization_Setup':
            result = True
            pNames = ['host', 'port', 'username', 'password', 'database']
            pHIT = {}
            totalResult = True

            re_pattern = {
                'host': [
                    '^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$',
                    '/^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$',
                    '^\S*(sock|socket)$'
                ],
                'port': ['^\d{3,5}$'],
                'username': ['^[a-zA-Z0-9_.-]{4,20}$'],
                'password': ['^[a-zA-Z0-9_.-]{4,20}$'],
                'database': ['^\S{8,30}$']
            }

            for xp in pNames:
                reg_hit = False
                for xr in range(len(re_pattern[xp])):
                    if xp == 'port':
                        if pHIT['host'] == 2:
                            reg_hit = True
                        else:
                            pass

                    else:
                        if re_search(re_pattern[xp][xr], param['data'][xp]) is not None:
                            pHIT[xp] = xr
                            reg_hit = True

                    if xp not in pHIT:
                        pHIT[xp] = None

                if not reg_hit:
                    if not result:
                        result = False
            result = True

        elif param['section'] == 'User_Registration':
            pass

            result = True

        return result
