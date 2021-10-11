from start import app
from zope.component import getUtility
from app.core.config import IManager
from app.libs.output import ITemplate
from flask import redirect

@app.route('/admin/<task>')
def hello_admin(task):
    if not getUtility(IManager).Tasks('checkConfig'):
        return redirect('/InitialSetup')
    else:
        # check session
        return "CheckSession"


