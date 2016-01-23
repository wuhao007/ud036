from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC867a50bd6933aa6358bae9105213a21c"
auth_token  = "1222afcaf4001f337ea3743a72885770"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="My name is Hao Wu?",
    to="+12063691582",    # Replace with your phone number
    from_="+13473219831") # Replace with your Twilio number
print message.sid
