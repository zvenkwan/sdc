'''
Created on Feb 27, 2018

@author: guan
'''
from twilio.rest import Client
account_sid = ""
auth_token  = ""
client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+13479949369", 
    from_="+19386666606",
    body="Hello from Python!")
print(message.sid)
