from flask import Blueprint
from flask_restx import Api

from resources.note.NoteResource import NoteResource
from resources.note.TaskResource import TaskResource
from resources.note.DiaryResource import DiaryResource

note_bp = Blueprint('noteApi', __name__,
                    static_folder='statics', static_url_path='/statics')
api = Api(note_bp)

api.add_resource(NoteResource, '/note')
api.add_resource(TaskResource, '/task', '/task/<int:taskId>')
api.add_resource(DiaryResource, '/diary', '/diary/<int:diaryId>')