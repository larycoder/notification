from flask_restful import Resource
from services.note_service import NoteService
from utils.http_util import HttpUtil
import json


class NoteController(Resource):
    def get(self):
        result = NoteService.get_note_list('*')
        result = json.dumps(result)

        return HttpUtil.get_response(result)