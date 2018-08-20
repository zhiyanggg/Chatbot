# from flask import Flask, request
# import json
#
# app = Flask(__name__)
#
# FB_API_URL = 'https://graph.facebook.com/v2.6/me/messages'
# VERIFY_TOKEN = 'nihao'
# PAGE_ACCESS_TOKEN = "EAACj6UD3ZBiMBAAkKkhcd2vXz7uHRrIiat2jhbK8Xm0GyHTu39zSJJNWL6apVxGZCYJxpZBjP5D8Kl2ATtTepRBCUAyFie1f4f0uPZBaNujV6TvH8htzzMF6FpjXLo26Jgq8vl0ZCi17H6yTYETyKqiyQ7Cj577woGxWLvdwYRo76darUo2AluroICzlJDTgZD"
#
#
# def get_bot_response(message):
#     """This is just a dummy function, returning a variation of what
#     the user said. Replace this function with one connected to chatbot."""
#     return "This is a dummy response to '{}'".format(message)
#
#
# def verify_webhook(req):
#     if req.args.get("hub.verify_token") == VERIFY_TOKEN:
#         return req.args.get("hub.challenge")
#     else:
#         return "incorrect"
#
# def respond(sender, message):
#     """Formulate a response to the user and
#     pass it on to a function that sends it."""
#     response = get_bot_response(message)
#     send_message(sender, response)
#
#
# def is_user_message(message):
#     """Check if the message is a message from the user"""
#     return (message.get('message') and
#             message['message'].get('text') and
#             not message['message'].get("is_echo"))
#
#
# @app.route("/",methods=['GET', 'POST'])
# def listen():
#     # GET: validate facebook token
# 	if request.method == 'GET':
# 		valid = messenger.verify_webhook(request)
# 		if not valid:
# 			abort(400, 'Invalid Facebook Verify Token')
# 		return valid
#
#     # POST: process message
# 	output = request.get_json()
# 	if 'entry' not in output:
# 		return 'OK'
#
# 	for entry in output['entry']:
# 		if 'messaging' not in entry:
# 			continue
#
# 		for item in entry['messaging']:
#
# 			# delivery notification (skip)
# 			if 'delivery' in item:
# 				continue
#
# 			# get user
# 			user = item['sender'] if 'sender' in item else None
# 			if not user:
# 				continue
# 			else:
# 				user_id = user['id']
#
# 			# handle event
# 			messenger.handle(user_id, item)
#
# 	return "ok"
# # @app.route('/get_movie_detail', methods=['POST'])
# #     def get_movie_detail():
# #         data = request.get_json(silent=True)
# #         movie = data['queryResult']
# #
# #
# #         response =  "Testing this out"
# #
# #         reply = {
# #             "fulfillmentText": response,
# #         }
# #
# #         return jsonify(reply)
#
# if __name__ == '__main__':
# 	app.run(debug=True, host='0.0.0.0')

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("queryResult").get("queryText") != "1 char kway teow 3 kopi":
        speech = "its here"
        return {
            "speech": speech,
            "displayText": speech,
            # "data": {},
            # "contextOut": [],
            "source": ""
        }

    # result = req.get("queryResult")
    # parameters = result.get("parameters")

    speech = "testing123"
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        "source": ""
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')