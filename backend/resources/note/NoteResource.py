from flask_restx import reqparse
from flask_restx import Resource

from repositories.NoteRepo import NoteRepo
from models.NoteModel import NoteModel
from models.ResponseModel import ResponseModel

from utils.JsonEncoder import JsonEncoder


class NoteResource(Resource):
    def get(self):
        repo = NoteRepo()
        data_list = repo.list_all()
        return JsonEncoder.encode(ResponseModel(data_list))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('subject', required=True, type=str)
        parser.add_argument('content', required=True, type=str)
        args = parser.parse_args()

        model = NoteModel()
        model.loadJSON(args)

        repo = NoteRepo()
        repo.add_object(model)
        repo.commit()
        return None