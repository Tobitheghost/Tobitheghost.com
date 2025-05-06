import os

image_dict = {"images":{
        "1": {
            "name":"",
            "title":"",
            "path":"",
            "instagram":"",
            "twitter":"",
            "mastadon":"",
            "linkedin":""},
        "2": {}
        }
    }

def load_images():
    list_of_images = os.listdir(os.path.abspath(os.path.join(".","website","static","pixel_art","images")))
