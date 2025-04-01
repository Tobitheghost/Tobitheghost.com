from flask import render_template, Blueprint, request, session, current_app, abort
import json

from ..errors import YouGotHigh, InfiniteLoop

utility = Blueprint('utility',__name__,template_folder="templates",static_folder="static")

@utility.route('/', methods=('GET', 'POST'))
def index():
    with open("website\\utility\\site.log", "r") as file:
        logs = file.read()
        str(repr(logs)).replace("\n", " ")
        print(logs)
    return render_template("utility/utility.html")

@utility.route('/admin', methods=('GET', 'POST'))
def admin():
    return render_template("utility/utility.html")

@utility.route('/errors/<int:code>', methods=('GET', 'POST'))
def errors(code):
    
    if code == 420:
        raise YouGotHigh()
    if code == 508:
        raise InfiniteLoop()
    
    print('\n',code,'\n')
    abort(code)