from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import time

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    listenMessage = request.form.get("Body")
    if listenMessage == "Hello":
        messageType = "Why so proper"
    elif listenMessage == "Hey":
        messageType = "Whatz uppp"
    elif listenMessage == "Hi":
        messageType = "Hi, how's your day been?"
    else:
        messageType = "Hello"
    resp = MessagingResponse()
    resp.message(messageType)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
