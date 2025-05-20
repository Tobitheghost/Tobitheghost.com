from flask import render_template, Blueprint, request, session, current_app, jsonify
from flask_cors import cross_origin
import logging

from .parcel_data import Parcel

logger = logging.getLogger('views')
parcel_viewer = Blueprint('parcel_viewer',__name__,static_folder="static",template_folder="templates")

@parcel_viewer.route("/maps")
def maps():
    logging.warn("parcel_viewer/maps.html")
    return render_template("parcel_viewer/maps.html")


@parcel_viewer.route("/search", methods=['POST', 'GEt'])
@cross_origin()
def search():
    data = request.args.get('address_input')
    logging.warn(data)
    
    if data:
        response_message = Parcel().search(data)
    else: 
        response_message = [
            {"id":"", "multipolygon": "", "address": ""}
        ]
    return render_template("parcel_viewer/search_results.html", results=response_message)

@parcel_viewer.route("/results/<addressID>", methods=['POST', 'GET'])
@cross_origin()
def results_(addressID):
    query = addressID
    logging.warn(addressID)
    if query:
        result = Parcel().viewer(query)
        return render_template("parcel_viewer/parcel_results.html", results=result)
    return render_template("parcel_viewer/parcel_results.html")