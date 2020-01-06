from flask_restful import Resource, request, reqparse

class Hello(Resource):
	def get(self):
		return {"message": "Hello, World!"}

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('command', type=str)
		args = parser.parse_args()
		command = args['command']
		return {"received": command}
