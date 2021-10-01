from flask import Flask


def init_app():
    app = Flask(__name__)

    # Simple hello view to init app
    @app.route('/hello')
    def hello():
        return 'hello'

    # Resource
    from resources.note import note_bp
    app.register_blueprint(note_bp, url_prefix="/notes")

    return app


if __name__ == '__main__':
    app = init_app()

    debug = True
    host = '0.0.0.0'
    port = 8080

    app.run(debug=debug, host=host, port=port)
