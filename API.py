from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask 
from dotenv import load_dotenv
import os

app = Flask(__name__)
# Encuentra tu Account SID y Auth Token en el Dashboard principal de Twilio

load_dotenv() 
TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
print(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

message = client.messages.create(
    from_='whatsapp:+17372508034',  # Tu número correcto del Sandbox
    body='¡Hola! Prueba de conexión con Python.',
    to='whatsapp:+573113651827'      # Tu número personal verificado
)

@app.route("/recibir-test", methods=["POST"])

def recibir_test():
  return f"Mensaje enviado con SID: {message.sid}"
