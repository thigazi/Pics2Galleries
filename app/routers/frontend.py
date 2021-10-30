from start import app
from app.core.config import IManager
from app.core.application import IPictureManager
from app.libs.output import ITemplate
from zope.component import getUtility
from flask import redirect, request
from json import dumps as json_dumps
from json import loads as json_loads


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
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            dset = json_loads(list(request.form.keys())[0])
            getUtility(IPictureManager).Tasks('verifyInput',{
                'section':'TestSection',
                'data':dset
            })
            return json_dumps({'hallo': 'tamer'})
