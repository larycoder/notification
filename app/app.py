from flask import Flask
from utils.log_util import Log_Util
import os

# routes
from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)
api = Api(bp)

# register controllers
from controllers.note_controller import (
    NotesController,
    NoteChildsController
)

api.add_resource(NotesController, '/notes')
api.add_resource(NoteChildsController, '/notes/<note_id>')

# start simple app
app = Flask(__name__)
app.register_blueprint(bp, url_prefix='/notification/v1')


if __name__ == '__main__':
    host = os.environ.get('HOST', '127.0.0.1')
    port = os.environ.get('PORT', 5000)
    debug = os.environ.get('DEBUG', True)
    app.run(host=host, port=port, debug=debug)