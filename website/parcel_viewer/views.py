from flask import render_template, Blueprint, request, session, current_app, jsonify
import logging

from .parcel_data import Parcel

logger = logging.getLogger('views')
parcel_viewer = Blueprint('parcel_viewer',__name__,static_folder="static",template_folder="templates")


@parcel_viewer.route("/maps")
def maps():
    logging.warn("parcel_viewer/maps.html")
    return render_template("parcel_viewer/maps.html")

@parcel_viewer.route("/search", methods=['POST'])
def search():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input'}), 400

        q_data = Parcel()
        response_message = q_data.search(data)

        return jsonify({'message': response_message}), 200  
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@parcel_viewer.route("/results/<addressID>", methods=['POST'])
def results_(addressID):
    query = addressID
    logging.warn(addressID)
    if query:
        q_data = Parcel()
        result = q_data.viewer(query)

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
        "effDate": effDate})