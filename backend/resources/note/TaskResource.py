from flask_restx import Resource, reqparse
from flask_restx import inputs

from repositories.TaskRepo import TaskRepo
from models.TaskModel import TaskModel
from models.ResponseModel import ResponseModel

from utils.JsonEncoder import JsonEncoder


class TaskResource(Resource):
    def get_list(self):
        repo = TaskRepo()
        data_list = repo.list_all()
        resp_data = JsonEncoder.encode(ResponseModel(data_list))
        # remove notes data
        for obj in resp_data["data"]:
            del obj["notes"]
        return resp_data

    def get_object(self, task_id):
        repo = TaskRepo()
        stmt = repo.select().where(TaskModel.id == task_id)
        obj = repo.execute(stmt).scalar_one()
        return JsonEncoder.encode(ResponseModel(obj))

    def get(self, taskId=None):
        if taskId is None:
            return self.get_list()
        else:
            return self.get_object(taskId)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task', required=True, type=str)
        parser.add_argument('parentId', type=int)
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

    def put(self, taskId):
        parser = reqparse.RequestParser()
        parser.add_argument('task', type=str)
        parser.add_argument('parentId', type=int)
        parser.add_argument('notes', type=str)
        parser.add_argument('label', type=str)
        parser.add_argument('priority', type=str)
        parser.add_argument('deadline', type=inputs.datetime_from_iso8601)
        parser.add_argument('measurement', type=str)
        parser.add_argument('process', type=float)

        args = parser.parse_args()
        args = {k:v for k, v in args.items() if v is not None}

        repo = TaskRepo()
        stmt = repo.select().where(TaskModel.id == taskId)
        model = repo.execute(stmt).scalar_one()
        model.loadJSON(args)
        repo.commit()
        return None

    def delete(self, taskId):
        repo = TaskRepo()
        stmt = repo.select().where(TaskModel.id == taskId)
        model = repo.execute(stmt).scalar_one()
        repo.delete_object(model)
        repo.commit()
        return None