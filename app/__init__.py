from flask import Flask
from app import routes


def create_app():
    app = Flask(__name__)

    app.config["JSON_SORT_KEYS"] = True

    routes.init_app(app)

    return app