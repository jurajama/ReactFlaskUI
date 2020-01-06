from flask_restful import Resource
import datetime

class Timeapi(Resource):
	def get(self):
	        return str(datetime.datetime.now()), 200	
