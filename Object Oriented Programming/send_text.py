from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC91653f2923e20fd3b01deeeb8a8c5e6a"
auth_token  = "878bae2ae80404763912cff4c467a58e"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="",
    to="+17174753140",    # Replace with your phone number
    from_="+17656370617") # Replace with your Twilio number
print message.sid
