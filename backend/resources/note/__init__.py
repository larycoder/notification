from flask import Blueprint
from flask_restx import Api

from resources.note.NoteResource import NoteResource

note_bp = Blueprint('noteApi', __name__,
                    static_folder='static', static_url_path='home')
api = Api(note_bp)

api.add_resource(NoteResource, '/notes')