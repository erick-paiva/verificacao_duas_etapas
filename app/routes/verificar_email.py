from flask import Blueprint
from app.controllers.verificar_email import cadastrar_email, verificar_email

bp_email = Blueprint("email", __name__, url_prefix="")


bp_email.post("/email")(verificar_email)
bp_email.post("/register")(cadastrar_email)
