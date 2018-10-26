# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console

def sendText(sendTo, message):
    account_sid = 'your account Sid'
    auth_token = 'your auth token'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=message,
             from_='+account number',
             to=sendTo
         )


    print(message.sid)
