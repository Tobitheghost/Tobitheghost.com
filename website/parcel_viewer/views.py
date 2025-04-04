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

@parcel_viewer.route("/results/<addressID>", methods=['POST'])
def results_(addressID):
    query = addressID
    logging.warn(addressID)
    if query:

        result = Parcel().viewer(query)

        address = result["full_address"]
        owner = result["owner_name"]
        owner2 = result["owner_name2"]
        land_use = result["landusecode"]
        land_desc = result["landusedesc"]
        asLandVal = result["assessed_land_value"]
        asImpVal = result["assessed_improved_value"]
        ExLandVal = result["exempt_land_value"]
        ExImpVal = result["exempt_improved_value"]
        effDate = result["assessment_effective_date"]
        poly = result["multipolygon"]

    return jsonify({
        "address": address,
        "owner": owner,
        "owner2": owner2,
        "land_use": land_use,
        "land_desc": land_desc,
        "asLandVal": asLandVal,
        "asImpVal": asImpVal,
        "ExLandVal": ExLandVal,
        "ExImpVal": ExImpVal,
        "effDate": effDate,
        "poly": poly})

# @parcel_viewer.route("/search", methods=['POST'])
# @cross_origin()
# def search():
#     try:
#         data = request.get_json()
#         logging.warn(data)
#         if not data:
#             logging.warn(f"error: Invalid input")
#             return jsonify({'error': 'Invalid input'}), 400

#         q_data = Parcel()
#         response_message = q_data.search(data)

#         return jsonify({'message': response_message}), 200  
#     except Exception as e:
#         logging.warn(f"error: {str(e)}")
#         return jsonify({'error': str(e)}), 500

# @parcel_viewer.route("/results/<addressID>", methods=['POST'])
# def results_(addressID):
#     query = addressID
#     logging.warn(addressID)
#     if query:
#         q_data = Parcel()
#         result = q_data.viewer(query)

#         address = result["full_address"]
#         owner = result["owner_name"]
#         owner2 = result["owner_name2"]
#         land_use = result["landusecode"]
#         land_desc = result["landusedesc"]
#         asLandVal = result["assessed_land_value"]
#         asImpVal = result["assessed_improved_value"]
#         ExLandVal = result["exempt_land_value"]
#         ExImpVal = result["exempt_improved_value"]
#         effDate = result["assessment_effective_date"]
#         poly = result["multipolygon"]

#     return jsonify({
#         "address": address,
#         "owner": owner,
#         "owner2": owner2,
#         "land_use": land_use,
#         "land_desc": land_desc,
#         "asLandVal": asLandVal,
#         "asImpVal": asImpVal,
#         "ExLandVal": ExLandVal,
#         "ExImpVal": ExImpVal,
#         "effDate": effDate,
#         "poly": poly})