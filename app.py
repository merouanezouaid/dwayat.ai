# Python libraries that we need to import for our bot

from flask import Flask, request
from pymessenger.bot import Bot
from bot_response import bot_response

app = Flask(__name__)
ACCESS_TOKEN = "EAAUk91XhuU0BO6RyvEMIkLZBvhs6vXUZCpYjyIeuCM78RJDLZBrZCjB43fvmoGtcAFhhJRmf8a0QGETxmvRRebEIysfMt7oxD7OhAMmncZBjjcukn6xwCPqzMkxZAF4dGHlM4VNifghidKEpD7rrZBKyB6WGFVuA9zZASpQnF84l68XB9RtFFInKxt22mjuk6NwPXCNRlgWqMropBuKm3gZDZD"
VERIFY_TOKEN = "dwayat.ai-verifytoken"
bot = Bot(ACCESS_TOKEN)

#  We will receive messages that Facebook sends our bot at this endpoint


@app.route("/", methods=['GET', 'POST'])
#  receive and send an answer message to the user
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    if message['message'].get('text'):
                        text = message['message'].get('text')
                        response_sent_text = bot_response(text)
                        send_message(recipient_id, response_sent_text)
                    # if user sends us a GIF, photo,video, or any other non-text item
                    if message['message'].get('attachments'):
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'



#  uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"


def get_message(message):
    """
    Process received non-text message and prepare a response.

    Parameters:
    message (dict): The received message.

    Returns:
    str: The response message.
    """
    # Check if the message contains an attachment
    if 'attachments' in message:
        attachment_type = message['attachments'][0]['type']
        if attachment_type == 'image':
            response = "You've sent an image."
        elif attachment_type == 'video':
            response = "You've sent a video."
        elif attachment_type == 'audio':
            response = "You've sent an audio."
        else:
            response = "You've sent an attachment."
    else:
        response = "I'm not sure how to process this message."

    return response

if __name__ == "__main__":
    app.run()
