import requests
import json
from flask import Flask, request, make_response
import dialogflow
import os
import spacy
from complexquery import *


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "foodbotntu-d20a8166c35d.json"
# os.environ [GCLOUD_PROJECT] = "foodbotntu"
# FB messenger credentials
ACCESS_TOKEN = "EAACj6UD3ZBiMBAOgOlZAvHPzdLXgSL5iBExwrZAcCOzEZCGzTo0Y1lZAoTucfNy4IFeGCWyuHXstsHPJuE4HZCb8hprJLZCskFXREzc3ZB87t0pJiC9bChB5ZBae2JfRQFcAveucRWhZCPzIfaN7BQNGcL0OfCsbG312ZB00EMeXARq7wZDZD"


# api.ai credentials
CLIENT_ACCESS_TOKEN = "4bb0bb44d60a4d8482af4d68c6224a39"
# ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
speech = ""

app = Flask(__name__)
listofdrinks = drinkslist()
print("finish loading drinks database data cache")
listoffood = foodlist()
print("finish loading food database data cache")
listofsides = sideslist()
print("finish loading sides database data cache")

@app.route('/', methods=['GET'])
def verify():
    # our endpoint echos back the 'hub.challenge' value specified when we setup the webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == 'nihao':
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return 'Hello World (from Flask!)', 200

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    print(message)
#     # prepare API.ai request
#     req = ai.text_request()
#     req.lang = 'en'  # optional, default value equal 'en'
#
#     #sending the query (message received)
#     req.query = message
#
#     # get response from API.ai
#     api_response = req.getresponse()
#
#     # decoding to utf-8 (converting byte object to json format)
#     responsestr = api_response.read().decode('utf-8')
#     response_obj = json.loads(responsestr) #loading it into json
#
# ##    if 'queryResult' in response_obj:
# ##        response = response_obj["queryResult"]["fulfillment"]["text"] #taking out the reply from json
# ##        reply(sender, response)
#
#     if response_obj["queryResult"]["intent"]["displayName"] == "Complexquery":
#         print("you got this right!")
#         response = "you got this right!" + str(response_obj["queryResult"]["fulfillment"]["text"])
#         reply(sender, response)
#
#     return "ok"
    global speech
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()
    project_id = "foodbotntu"
    session_id = sender
    language_code = "en-US"
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    # for text in message:
    text_input = dialogflow.types.TextInput(
    text=message, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
        session=session, query_input=query_input)

    # print('=' * 20)
    #     # print('Query text: {}'.format(response.query_result.query_text))
    #     # print('Detected intent: {} (confidence: {})\n'.format(
    #     #     response.query_result.intent.display_name,
    #     #     response.query_result.intent_detection_confidence))
    #     # print('Fulfillment text: {}\n'.format(
    #     #     response.query_result.fulfillment_text))

    intentofDF = response.query_result.intent.display_name
    if intentofDF == "Complexquery":
        speech = complexq(response.query_result.query_text)
        result = {
            "fulfillmentText": speech,
            # "source": "facebook",
                "fulfillmentMessages": [
                    # {
                    #     "platform": "FACEBOOK",
                    #     "card": {
                    #         "title": "Title: this is a title",
                    #         "subtitle": "This is an subtitle.  Text can include unicode characters including emoji 📱.",
                    #         "imageUri": "https://developers.google.com/actions/images/badges/XPM_BADGING_GoogleAssistant_VER.png",
                    #         "buttons": [
                    #             {
                    #                 "text": "This is a button",
                    #                 "postback": "https://assistant.google.com/"
                    #             }
                    #         ]
                    #     }
                    # },
                    {
                        "platform": "FACEBOOK",
                        "text": {
                            "text": [
                                speech
                            ]
                        }
                    }
                ],
            }
        reply(sender, speech)

    elif intentofDF == "Complexquery - yes":
        processedorder = totalprice()
        # result = {
        #     "fulfillmentText": processedorder,
        #     # "source": "facebook",
        #     "fulfillmentMessages": [
        #         {
        #             "platform": "FACEBOOK",
        #             "text": {
        #                 "text": [
        #                     "The total price for your order is $", processedorder
        #                 ]
        #             }
        #         }
        #     ],
        # }
        reply(sender, "The total price for your order is $"+str(round(processedorder, 2)))

    elif intentofDF == "list_drink":
        # result = {
        #     "fulfillmentMessages": [
        #         {
        #             "platform": "FACEBOOK",
        #             "text": {
        #                 "text": [
        #                     "We have the following sides: ", drinkslist()
        #                 ]
        #             }
        #         }
        #     ],
        # }
        reply(sender, "We have the following drinks: \u000A"+listofdrinks)

    elif intentofDF == "list_side_dishes":
        # result = {
        #     "fulfillmentMessages": [
        #         {
        #             "platform": "FACEBOOK",
        #             "text": {
        #                 "text": [
        #                     "We have the following sides: ", sideslist()
        #                 ]
        #             }
        #         }
        #     ],
        # }
        reply(sender, "We have the following sides: \u000A"+listofsides)

    elif intentofDF == "list_food_by_cuisine":
        # result = {
        #     "fulfillmentMessages": [
        #         {
        #             "platform": "FACEBOOK",
        #             "text": {
        #                 "text": [
        #                     "We have the following food: ", foodlist()
        #                 ]
        #             }
        #         }
        #     ],
        # }
        reply(sender,  "We have the following food: \u000A"+listoffood)

    else:
        reply(sender, response.query_result.fulfillment_text)
    # reply(sender, json.dumps(result, indent=4))
    return 'OK'

# def webhook(result):
#     res = json.dumps(result, indent=4)
#     print(res)
#     r = make_response(res)
#     r.headers['Content-Type'] = 'application/json'
#     data = request.json
#     sender = data['entry'][0]['messaging'][0]['sender']['id']
#     speechtoreturn = reply(sender, r)
#
#     return speechtoreturn

if __name__ == '__main__':
    app.run(debug=True)
