from flask_restful import Resource
from flask import request

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
        result = NoteService.get_note_info(note_id)
        result = json.dumps(result)
        return HttpUtil.get_response(result)


class NewNoteController(Resource):
    def post(self):
        header, body = HttpUtil.get_request(request)

        parent_id = body['parent_id'] if 'parent_id' in body else None
        note_name = body['note_name']
        
        result = NoteService.add_new_note(note_name, parent_id)
        result = json.dumps(result)
        return HttpUtil.get_response(result)