from flask import Flask
from flask_restx import Api

app = Flask(__name__)
api = Api(
    app,
    version="0.1",
    title="Notification API",
    description="Data API",
)
app.app_context().push()
