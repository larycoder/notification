from flask_restx import Resource


class NoteResource(Resource):
    def get(self):
        return "Hello note resource."