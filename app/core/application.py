from zope.interface import Interface
from zope.interface import implementer
from re import search as re_search


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

    def ActionHandler(self, app, task, params):
        rset = None
        if app == 'verifyInput':
            rset = self.__verifyInput(task, params)

        return rset

    def __verifyInput(self, action_type, param):
        result = None
        if action_type == 'Initialization_Setup':
            pNames = ['host', 'port', 'username', 'pass', 'dbname']
            totalResult = True
            re_pattern = [
                [
                    '^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$',
                    '/^\s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)){3}))|:)))(%.+)?\s*$',
                    '^\S*\.socket$'
                ],
                '^\d{3,5}$',
                '^[a-zA-Z0-9_.-]{4,20}$',
                '^[a-zA-Z0-9_.-]{4,20}$',
                '^\S{8,30}$'
            ]

            for i in range(5):
                if i == 0:
                    if (re_search(re_pattern[0][0], param[pNames[i]]) is None & re_search(re_pattern[0][1], param[pNames[i]]) is None & re_search(re_pattern[0][2], param[pNames[i]]) is None):
                        totalResult = False
                else:
                    if re_search(re_pattern[0][0], param[pNames[i]]) is None:
                        totalResult = False
            result = totalResult

        elif action_type == 'User_Registration':
            pass

        return result
