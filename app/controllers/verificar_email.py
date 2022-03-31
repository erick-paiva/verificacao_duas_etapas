from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from http import HTTPStatus
from email.message import EmailMessage
import os
from random import randint
import smtplib
from flask import jsonify, request
from app.controllers.email_content_html import HTML
import email.message

from app.models.verificar_email import Email

def gerar_codigo():
    return randint(1000, 9999)

def cadastrar_codigo_e_email_no_banco(email, code):
    
    
    pass

def mandar_email (user_email: str, code:int):
    senha = os.getenv("EMAIL_PASSWORD")
    
    msg = MIMEMultipart()
    # msg = EmailMessage()
    msg['From'] = "erickpaivaasilva@gmail.com"
    msg['To'] = user_email
    msg['Subject'] = "verificação de email"
    msg.add_header('Content-Type', 'text/html')
    # msg.attach(MIMEText("Seu código de verificação é: %s" % code, 'plain'))
    # msg.set_payload(HTML2.encode('utf-8'))
    # msg.set_content("oi")
    msg.attach(MIMEText(HTML, 'html'))
    # msg.add_alternative(HTML2.format(test="oi", subtype='html'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(msg["from"], senha)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    
    # return [code, email]


def verificar_email():
    Email.create_table_if_not_exits()
    data = request.get_json()
    code = gerar_codigo()
    codigo_verificado = Email.obter_um_codigo_por_email(data["email"])
    
    if not data.get("code"):
        mandar_email(data["email"], code)
        
    try:
        if data["code"] == codigo_verificado:
            return jsonify({"message": "Código correto"}), HTTPStatus.OK
        else:
            return {"message": "Código incorreto"}, HTTPStatus.BAD_REQUEST
    except:
        pass
    
    try:
        user = Email(code, data["email"])
        user.create_user()
    except Exception as e:
        Email.atualizar_code_por_email(data["email"], code)
        print("deu ruim", e)
    
    
        
   
    
    return {}, HTTPStatus.NO_CONTENT

