from flask_restx import Resource, reqparse
from flask_restx import inputs

from repositories.TaskRepo import TaskRepo
from models.TaskModel import TaskModel
from models.ResponseModel import ResponseModel

from utils.JsonEncoder import JsonEncoder


class TaskResource(Resource):
    def get(self):
        repo = TaskRepo()
        data_list = repo.list_all()
        return JsonEncoder.encode(ResponseModel(data_list))

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task', required=True, type=str)
        parser.add_argument('notes', type=str)
        parser.add_argument('label', type=str)
        parser.add_argument('priority', type=str)
        parser.add_argument('deadline', type=inputs.datetime_from_iso8601)
        parser.add_argument('measurement', type=str)
        parser.add_argument('process', type=float)

        args = parser.parse_args()

        model = TaskModel()
        model.loadJSON(args)

        repo = TaskRepo()
        repo.add_object(model)
        repo.commit()
        return None
