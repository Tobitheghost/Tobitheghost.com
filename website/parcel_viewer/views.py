from flask import render_template, Blueprint, request, session, current_app
import logging

from .parcel_data import Parcel

logger = logging.getLogger('views')
parcel_viewer = Blueprint('parcel_viewer',__name__,template_folder="templates",static_folder="static")


@parcel_viewer.route("/maps")
def maps():
    logging.warn("parcel_viewer/maps.html")
    return render_template("parcel_viewer/maps.html")

@parcel_viewer.route("/search")
def search_s():
    query = request.args.get("q")
    q_data = Parcel()
    logging.warn(query)
    if query:
        result = q_data.search(query)
    else:
        result = [
            {"id": "error", "multipolygon": "error", "address": "something went wrong"}
        ]

    return render_template("parcel_viewer/search_results.html", results=result)

@parcel_viewer.route("/results/<addressID>")
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

    return render_template(
        "parcel_viewer/parcel_results.html",
        address=address,
        owner=owner,
        owner2=owner2,
        land_use=land_use,
        land_desc=land_desc,
        asLandVal=asLandVal,
        asImpVal=asImpVal,
        ExLandVal=ExLandVal,
        ExImpVal=ExImpVal,
        effDate=effDate,
    )