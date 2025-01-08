import os
from dotenv import load_dotenv # para cangar el entorno virual
from email.message import EmailMessage
import ssl
import smtplib

load_dotenv()

email_sender = "fichadormensual@gmail.com"
password = os.getenv("PASSWORD")
email_reciver = "paniaguaaf82001@gmail.com"

subject = "Este es un asunto de prueba"
body = "Este es un cuerpo de prueba"

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(email_sender, password)
    smtp.sendmail(email_sender, email_reciver,em.as_string())

print("Correo enviado")
