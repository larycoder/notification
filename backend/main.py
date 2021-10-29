from flask import Flask, send_file
from flask import Blueprint
from resources.note import note_bp


def init_app():
    app = Flask(__name__)

    # Simple hello view to init app
    @app.route('/hello')
    def hello():
        return 'hello'

    @app.route('/favicon.ico')
    def favicon():
        return send_file('favicon.ico')

    # Blueprint for statics folder
    static_bp = Blueprint(
        'statics', __name__,
        static_folder='statics',
        static_url_path='/statics'
    )
    app.register_blueprint(static_bp)

    # Resource
    app.register_blueprint(note_bp, url_prefix="/noteApi")

    return app


if __name__ == '__main__':
    app = init_app()

    debug = True
    host = '0.0.0.0'
    port = 8080

    app.run(debug=debug, host=host, port=port)
