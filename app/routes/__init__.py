from flask import Flask, Blueprint
from .verificar_email import bp_email

# bp = Blueprint("api", __name__)


def init_app(app: Flask):
    app.register_blueprint(bp_email)
    # app.register_blueprint(bp)