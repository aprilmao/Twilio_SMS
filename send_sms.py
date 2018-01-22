# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACf31750ad1955ba6a5fb7c8f6d60e0a37"
auth_token = "1ac46a5361701102902f8937a15e2b51"
client = Client(account_sid, auth_token)

client.messages.create(to="+14083757798",
                       from_="+12672140128",                                                           body="Hello there!")
