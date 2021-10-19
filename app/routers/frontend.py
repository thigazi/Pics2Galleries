from start import app
from app.core.config import IManager
from app.libs.output import ITemplate
from zope.component import getUtility
from flask import redirect, request
from json import dumps as json_dumps


@app.route('/')
def hello_frontend():
    if not getUtility(IManager).Tasks('checkConfig'):
        return redirect('/InitialSetup')

    else:
        return "Main Page"


@app.route('/InitialSetup',methods=['GET','POST'])
def setup_app():
    if request.method == 'GET':
        return getUtility(ITemplate).render('frontend.init.html',{})
    elif request.method == 'POST':
        print(request.form)
        return json_dumps({'hallo': 'tamer'})
