from flask import Flask, Blueprint
from .series import bp_series
from .verificar_email import bp_email

bp = Blueprint("api", __name__, url_prefix="/api")


def init_app(app: Flask):
    bp.register_blueprint(bp_series)
    bp.register_blueprint(bp_email)
    app.register_blueprint(bp)