from flask import Blueprint
from flask_restx import Api

from resources.note.NoteResource import NoteResource
from resources.note.TaskResource import TaskResource
from resources.note.DiaryResource import DiaryResource

note_bp = Blueprint('noteApi', __name__,
                    static_folder='static', static_url_path='home')
api = Api(note_bp)

api.add_resource(NoteResource, '/note')
api.add_resource(TaskResource, '/task')
api.add_resource(DiaryResource, '/diary')