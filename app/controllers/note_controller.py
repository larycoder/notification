from flask_restful import Resource
from services.note_service import NoteService
from utils.http_util import HttpUtil
import json


class NotesController(Resource):
    def get(self):
        result = NoteService.get_note_list('*')
        result = json.dumps(result)
        return HttpUtil.get_response(result)


class NoteChildsController(Resource):
    def get(self, note_id):
        result = NoteService.get_note_child(note_id)
        result = json.dumps(result)
        return HttpUtil.get_response(result)