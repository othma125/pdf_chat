#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api')

from api.views.users import *
from api.views.documents import *
from api.views.text_blocks import *
# from api.views.places import *
# from api.views.places_reviews import *
# from api.views.cities import *
# from api.views.amenities import *
# from api.views.places_amenities import *
