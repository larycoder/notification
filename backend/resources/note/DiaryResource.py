from flask_restx import Resource, reqparse
from flask_restx import inputs

from repositories.DiaryRepo import DiaryRepo
from models.DiaryModel import DiaryModel
from models.ResponseModel import ResponseModel

from utils.JsonEncoder import JsonEncoder
from utils.TimeUtil import TimeUtil


class DiaryResource(Resource):
    def get_list(self):
        repo = DiaryRepo()
        data_list = repo.list_all()
        resp_data = JsonEncoder.encode(ResponseModel(data_list))
        # remove notes data
        for obj in resp_data["data"]:
            del obj["notes"]
        return resp_data

    def get_obj(self, diary_id):
        repo = DiaryRepo()
        stmt = repo.select().where(DiaryModel.id == diary_id)
        obj = repo.execute(stmt).scalar_one()
        return JsonEncoder.encode(ResponseModel(obj))

    def get(self, diaryId=None):
        if diaryId is None:
            return self.get_list()
        else:
            return self.get_obj(diaryId)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('activity', required=True, type=str)
        parser.add_argument('notes', type=str)
        parser.add_argument('start_time', type=inputs.datetime_from_iso8601)
        parser.add_argument('duration', type=str)
        parser.add_argument('taskId', type=int)
        args = parser.parse_args()

        args['duration'] = TimeUtil.str_to_second(args['duration'])

        model = DiaryModel()
        model.loadJSON(args)

        repo = DiaryRepo()
        repo.add_object(model)
        repo.commit()
        return None
