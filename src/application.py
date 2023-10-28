from flask import Flask, Blueprint
from flask_restx import Api

app = Flask(__name__)
api_bp = Blueprint("api", __name__, url_prefix="/api/")
api = Api(
    api_bp,
    version="0.1",
    title="Notification API",
    description="Data API",
)
app.register_blueprint(api_bp)
app.app_context().push()


@app.route("/")
def greet():
    my_greet = {
        "Greeting": "Welcome to Notification application",
        "Front-end link": "/static/index.html",
        "Swagger link": "/api",
    }
    return my_greet, 200
