from start import app
from app.core.config import IManager
from zope.component import getUtility


@app.route('/')
def hello_frontend():
    print(getUtility(IManager).Tasks('checkConfig'))
    return "this is the frontend"


@app.route('/InitialSetup')
def setup_app():
    return "This is the Setup Page"
