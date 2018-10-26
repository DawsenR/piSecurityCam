# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console

def sendText(sendTo, message, image = 0):
    account_sid = 'AC46f131b5abd9b319efc9514bd0f4f7ea'
    auth_token = '2252316456898b4dec75a2b2856a358f'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
             body=message,
             from_='+18174978517',
             #media_url=image,
             to=sendTo
         )

    print(message.sid)
