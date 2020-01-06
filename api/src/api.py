'''
Defines custom Flask Blueprint for the /api/ resource prefix & all subroutes
'''

from flask import Blueprint
from flask_restful import Api
from resources.hello import Hello
from resources.timeapi import Timeapi

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes
api.add_resource(Hello, '/hello')
api.add_resource(Timeapi, '/time')
