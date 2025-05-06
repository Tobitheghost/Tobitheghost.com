from flask import render_template, Blueprint, request, session, current_app, abort
import json, os

from ..errors import YouGotHigh, InfiniteLoop

utility = Blueprint('utility',__name__,template_folder="templates",static_folder="static")

@utility.route('/', methods=('GET', 'POST'))
def index():
    with open("website\\utility\\site.log", "r") as file:
        logs = file.read()
        str(repr(logs)).replace("\n", " ")
        print(logs)
    return render_template("utility/utility.html")

# @utility.route('/pixelart', methods=('GET', 'POST'))
# def pixelart():
#     # data = None
#     with open(os.path.abspath(os.path.join(".","website","pixel_art","images.json"))) as file:
#         data = json.load(file)
#         for x in data["images"].keys():
#             print("fuck", data['images'][x]['thumbnail'])
        
#     return render_template("utility/pixelart.html", imgs=data["images"])

@utility.route('/pixelart', methods=('GET', 'POST'))
def pixelart():

    list_of_images = os.listdir(os.path.abspath(os.path.join(".","website","static","pixel_art","images","gallery")))
    
    return render_template("utility/pixelart.html", imgs=list_of_images)

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