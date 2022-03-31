from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import HTTPStatus
import os
from random import randint
import smtplib
from flask import jsonify, request
from app.controllers.email_content_html import HTML
from app.models.verificar_email import Email


def gerar_codigo():
    return randint(100000, 999999)


def mandar_email(user_email: str, code: int):
    senha = os.getenv("EMAIL_PASSWORD")
    msg = MIMEMultipart()
    msg['From'] = "erickpaivaasilva@gmail.com"
    msg['To'] = user_email
    msg['Subject'] = "verificação de email"
    msg.add_header('Content-Type', 'text/html')
    msg.attach(MIMEText(HTML.format(code=code), 'html'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg["from"], senha)
    server.sendmail(msg['From'], msg['To'], msg.as_string())

def cadastrar_email():
    Email.create_table_if_not_exits()
    code = gerar_codigo()
    data = request.get_json()
    try:
        user = Email(code, data["email"])
        user.create_user()
        mandar_email(data["email"], code)
    except Exception as e:
        Email.atualizar_code_por_email(data["email"], {"code": code})
        print("deu ruim", e)
        return jsonify({"message": "Email já cadastrado"}), HTTPStatus.CONFLICT

    return {}, HTTPStatus.NO_CONTENT

def verificar_email():
    Email.create_table_if_not_exits()
    data = request.get_json()
    code = gerar_codigo()
    codigo_verificado = Email.obter_codigo_ou_tentativas_por_email(data["email"])
    tentativas = Email.obter_codigo_ou_tentativas_por_email(
        data["email"], ["tentativas"])
    
    if not codigo_verificado:
        return jsonify({"message": "Email não cadastrado"}), HTTPStatus.NOT_FOUND

        
    if tentativas["tentativas"] == 0:
        Email.atualizar_code_por_email(data["email"], {"tentativas": 3, "code": code})
        mandar_email(data["email"], code)
        return jsonify({"message": "tentativas esgostadas vamos mandar outro codigo"}), HTTPStatus.TOO_MANY_REQUESTS


    if data["code"] == codigo_verificado["code"]:
        return jsonify({"message": "Código correto"}), HTTPStatus.OK
    else:
        # update no banco e diminuir o numero de tentativas
        # e se caso o numero de tentativas for 0, mandar um novo codigo
        Email.atualizar_code_por_email(data["email"], {"tentativas": tentativas["tentativas"]-1})
        
        return {"message": "Código incorreto"}, HTTPStatus.BAD_REQUEST

    # return {}, HTTPStatus.NO_CONTENT
