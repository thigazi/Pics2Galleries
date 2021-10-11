from start import app
from app.core.config import IManager
from app.libs.output import ITemplate
from zope.component import getUtility
from flask import redirect


@app.route('/')
def hello_frontend():
    if not getUtility(IManager).Tasks('checkConfig'):
        return redirect('/InitialSetup')

    else:
        return "Main Page"


@app.route('/InitialSetup')
def setup_app():
    return getUtility(ITemplate).render('frontend.init.html',{})
