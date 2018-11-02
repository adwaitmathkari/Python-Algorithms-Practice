# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 15:57:25 2018

@author: Adwait
"""

#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAFL2QZCujZC4BAL28M1t5gCDEr4jbilVsPxhqK6GMyqOm4q8de5wIeC0hS8WaLlZB9AihWIQyEcKP3YJEk3FoCmVhDSP0xiobI6bGZCi0yjVAB4vZAIKK8xCILOVnjhHloGDwIQhWxt44nZCpi0smcaGCFwhwlI00RV84DZCUAdUWA4w4GaZBKR'
VERIFY_TOKEN = 'pybot1326'
bot = Bot(ACCESS_TOKEN)

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, 
    #it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
       output = request.get_json()
#       print(output)
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                #Facebook Messenger ID for user so we know where to send response back to
                recipient_id = message['sender']['id']
                imageurl="http://guardianlv.com/wp-content/uploads/2014/03/Robots-The-Possibilities-of-Artificial-Intelligence.jpg"
                if message['message'].get('text'):
                    bot.send_image_url(recipient_id,imageurl)
                    response_sent_text = get_message()                    
                    send_message(recipient_id, response_sent_text)
                    
                #if user sends us a GIF, photo,video, or any other non-text item
                if message['message'].get('attachments'):
                    bot.send_image_url(recipient_id,imageurl)
                    response_sent_nontext = get_message2()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


#chooses a random message to send to the user
def get_message():
    sample_responses = ["Thank You for contacting us we will get back soon!", "We're getting back you in some time.", "Hello, Glad you contacted us! We'll get back soon!", "We're greatful to know you, we'll get back soon!"]
    # return selected item to the user
    return random.choice(sample_responses)

def get_message2():
    sample_responses = ["HI THERE, Thank You for contacting us we will get back soon!", "HI THERE, We're getting back you in some time.", "HI THERE, Hello, Glad you contacted us! We'll get back soon!", "HI THERE, We're greatful to know you, we'll get back soon!"]
    # return selected item to the user
    return random.choice(sample_responses)

#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()


#
#use ngrok to initiate an online server
#in the terminal enter "C:\Program Files\ngrok" http 5000
#and the server goes live 
#further we give this address to facebook and it will send us the messages to this place 
#this server will send this message to our python made http:\\127.0.0.1:5000 made by the flask app
#now we get this request as either POST or GET and we further process these requests
#a GET request is checked whether it has the the right verification code 
#request.args.get('hub.verify_token') the extension hub.verify_token mostly belongs to facebook
#further if the token is verified we return request.args.get('hub.challenge')
#what exactly is this is i dont know but it is probably something some 
#acceptance code that we return on our http://127.. and it is carried to facebook via ngrok
#now in a POST request.get_json() is used. it is a dictionary which has atleast some of the following structure
#output={'entry':{'event1':{'messaging':{'message':{'sender':{'id':recipient_id}}}},'event2':{'messaging':{'message':{'sender':{'id':recipient_id}}}},}
#
#output is actually 
#{'object': 'page', 'entry': [{'id': '159025678128985', 'time': 1521480653088, 'messaging': [{'sender': {'id': '1599851063468048'}, 'recipient': {'id': '159025678128985'}, 'timestamp': 1521480633803, 'message': {'mid': 'mid.$cAADKUTdtiWlocJVVy1iP1AQsP-p8', 'seq': 8706, 'text': 'hello how re you'}}]}]}
#event in output['entry'] thus event=[{'id': '159025678128985', 'time': 1521480653088, 'messaging': [{'sender': {'id': '1599851063468048'}, 'recipient': {'id': '159025678128985'}, 'timestamp': 1521480633803, 'message': {'mid': 'mid.$cAADKUTdtiWlocJVVy1iP1AQsP-p8', 'seq': 8706, 'text': 'hello how re you'}}]}]
#messaging=[{'sender': {'id': '1599851063468048'}, 'recipient': {'id': '159025678128985'}, 'timestamp': 1521480633803, 'message': {'mid': 'mid.$cAADKUTdtiWlocJVVy1iP1AQsP-p8', 'seq': 8706, 'text': 'hello how re you'}}]
#message in messageing
#thus message={'sender': {'id': '1599851063468048'}, 'recipient': {'id': '159025678128985'}, 'timestamp': 1521480633803, 'message': {'mid': 'mid.$cAADKUTdtiWlocJVVy1iP1AQsP-p8', 'seq': 8706, 'text': 'hello how re you'}}
#
#now we check if a message was sent and 
#we send back a message using Bot.send_text_message(recipient_id, response)

    
