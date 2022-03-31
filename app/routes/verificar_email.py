from flask import Blueprint
from app.controllers.verificar_email import verificar_email

bp_email = Blueprint("email", __name__, url_prefix="/email")


bp_email.post("")(verificar_email)
