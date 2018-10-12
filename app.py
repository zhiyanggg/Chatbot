import requests
import json
from flask import Flask, request, make_response
import dialogflow
import os
import spacy
from complexquery import *
from foodlistcards import *

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "foodbotntu-d20a8166c35d.json"
# FB messenger credentials
ACCESS_TOKEN = "EAACj6UD3ZBiMBAOgOlZAvHPzdLXgSL5iBExwrZAcCOzEZCGzTo0Y1lZAoTucfNy4IFeGCWyuHXstsHPJuE4HZCb8hprJLZCskFXREzc3ZB87t0pJiC9bChB5ZBae2JfRQFcAveucRWhZCPzIfaN7BQNGcL0OfCsbG312ZB00EMeXARq7wZDZD"


# api.ai credentials
CLIENT_ACCESS_TOKEN = "4bb0bb44d60a4d8482af4d68c6224a39"
speech = ""

app = Flask(__name__)
listofdrinks = drinkslist()
print("finish loading drinks database data cache")
listoffood = foodlist()
print("finish loading food database data cache")
listofsides = sideslist()
print("finish loading sides database data cache")

info = []
postbackfood = ""
postbackfoodorder = ""

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
    global speech, info
    global postbackfoodorder
    global postbackfood
    import dialogflow_v2 as dialogflow

    # data = request.json
    data = request.get_json()
    if data["object"] == "page":
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("postback"):
                    # user clicked/tapped "postback" button in earlier message
                    message_text = messaging_event["postback"]["payload"]
                    # the button's payload
                    print("Inside postback")
                    print("this is message_Text: ", message_text)
                    sender_id = messaging_event["sender"]["id"]
                    if message_text:
                        if message_text == "list of food":
                            reply(sender_id, foodpage1(ACCESS_TOKEN, sender_id))
                            return 'OK'

                        elif message_text == "list of drinks":
                            reply(sender_id, drinkspage1(ACCESS_TOKEN, sender_id))
                            return 'OK'

                        elif message_text == "list of sides":
                            reply(sender_id, sidespage1(ACCESS_TOKEN, sender_id))
                            return 'OK'

                        elif message_text == "View More food page 2":
                            reply(sender_id, foodpage2(ACCESS_TOKEN,sender_id))
                            return 'OK'

                        elif message_text == "View More food page 3":
                            reply(sender_id, foodpage3(ACCESS_TOKEN,sender_id))
                            return 'OK'

                        elif message_text == "View More food page 4":
                            reply(sender_id, foodpage4(ACCESS_TOKEN,sender_id))
                            return 'OK'

                        elif message_text == "View More food page 5":
                            reply(sender_id, foodpage5(ACCESS_TOKEN,sender_id))
                            return 'OK'

                        elif message_text == "View More drinks page 2":
                            reply(sender_id, drinkspage2(ACCESS_TOKEN,sender_id))
                            return 'OK'

                        else:
                            postbackfood += ''.join([i for i in message_text if not i.isdigit()])
                            reply(sender_id, "How many " + postbackfood + " do you wish to order?")
                            return 'OK'



    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
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
        # speech = complexq(response.query_result.query_text, "needclean")
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
        # reply(sender, "The total price for your order is $"+str(round(processedorder, 2)))
        reply(sender, str(processedorder))

    elif intentofDF == "ask_menu_word":
        menu = "----------------------------"
        menu += "\u000A"
        menu += "Food:"
        menu += "\u000A"
        menu += "----------------------------"
        menu += "\u000A"
        menu += listoffood
        menu += "\u000A"
        menu += "----------------------------"
        menu += "\u000A"
        menu += "Drinks:"
        menu += "\u000A"
        menu += "----------------------------"
        menu += "\u000A"
        menu += listofdrinks
        menu += "\u000A"
        menu += "----------------------------"
        menu += "\u000A"
        menu += "Sides:"
        menu += "\u000A"
        menu += "----------------------------"
        menu += "\u000A"
        menu += listofsides
        reply(sender, menu)

    elif intentofDF == "ask_menu":
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                          params={"access_token": ACCESS_TOKEN},
                          data=json.dumps({
                              "recipient": {
                                  "id": sender
                              },
                              "message": {
                                  "attachment": {
                                      "type": "template",
                                      "payload": {
                                          "template_type": "generic",
                                          "elements": [
                                              {
                                                  "title": "FOOD",
                                                  "image_url": "https://cdn.citynomads.com/wp-content/uploads/2017/06/08154455/straits-kitchen-cover3.png",
                                                  "subtitle": "Main dishes for everyone. Contains Chinese, Indian, Western,Malay to Indian Food!",
                                                  "buttons": [
                                                      {
                                                          "type": "postback",
                                                          "title": "Browse Food Menu",
                                                          "payload": "list of food"
                                                      }
                                                  ]
                                              },
                                              {
                                                  "title": "DRINKS",
                                                  "image_url": "https://cdn.greatdeals.com.sg/wp-content/uploads/2018/04/23223453/tuk-tuk-cha-1-for-1-all-beverages-offer-april-2018-628x419.jpg",
                                                  "subtitle": "Beverages suited for you from hot to cold!",
                                                  "buttons": [
                                                      {
                                                          "type": "postback",
                                                          "title": "Browse Drinks Menu",
                                                          "payload": "list of drinks"
                                                      }
                                                  ]
                                              },
                                              {
                                                  "title": "SIDES",
                                                  "image_url": "https://d1f28u9l1tudce.cloudfront.net/apps/_shared/sides.jpg",
                                                  "subtitle": "Mini finger food for you to snack your day away!",
                                                  "buttons": [
                                                      {
                                                          "type": "postback",
                                                          "title": "Browse Sides Menu",
                                                          "payload": "list of sides"
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                  }
                              }
                          }),
                          headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print(r.text)

    elif intentofDF == "list_drink":
        reply(sender, drinkspage1(ACCESS_TOKEN, sender))

    elif intentofDF == "list_side_dishes":
        reply(sender, sidespage1(ACCESS_TOKEN, sender))

    elif intentofDF == "list_food_by_cuisine":
        reply(sender, foodpage1(ACCESS_TOKEN, sender))

    elif intentofDF == "ask_food_description":
        print("parameters is ", response.query_result.parameters, "type is ", type(response.query_result.parameters))
        print("food item is", response.query_result.parameters['foods'])
        info = fooddetails(response.query_result.parameters['foods'])
        print("item info is ", info)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                          params={"access_token": ACCESS_TOKEN},
                          data=json.dumps({
                              "recipient": {
                                  "id": sender
                              },
                              "message": {
                                  "attachment": {
                                      "type": "template",
                                      "payload": {
                                          "template_type": "generic",
                                          "elements": [
                                              {
                                                  "title": (info[0]+" : $"+str(info[1])),
                                                  "image_url": info[3],
                                                  "subtitle": (info[2] + " The price of the food is " + str(info[1])),
                                                  "default_action": {
                                                      "type": "web_url",
                                                      "url": info[3],
                                                      "webview_height_ratio": "tall",
                                                  },
                                                  "buttons": [
                                                      {
                                                          "type": "postback",
                                                          "title": "Order now",
                                                          "payload": info[0]
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                  }
                              }
                          }),
                          headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print(r.text)

    elif intentofDF == "ask_drinks_description":
        print("parameters is ", response.query_result.parameters, "type is ", type(response.query_result.parameters))
        print("Drink item is", response.query_result.parameters['drinks'])
        info = drinksdetails(response.query_result.parameters['drinks'])
        print("item info is ", info)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                          params={"access_token": ACCESS_TOKEN},
                          data=json.dumps({
                              "recipient": {
                                  "id": sender
                              },
                              "message": {
                                  "attachment": {
                                      "type": "template",
                                      "payload": {
                                          "template_type": "generic",
                                          "elements": [
                                              {
                                                  "title": (info[0] + " : $" + str(info[1])),
                                                  "image_url": info[3],
                                                  "subtitle": (info[2] + " The price of the drinks is " + str(info[1])),
                                                  "default_action": {
                                                      "type": "web_url",
                                                      "url": info[3],
                                                      "webview_height_ratio": "tall",
                                                  },
                                                  "buttons": [
                                                      {
                                                          "type": "postback",
                                                          "title": "Order now",
                                                          "payload": info[0]
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                  }
                              }
                          }),
                          headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print(r.text)

    elif intentofDF == "ask_sides_description":
        print("parameters is ", response.query_result.parameters, "type is ", type(response.query_result.parameters))
        print("side item is", response.query_result.parameters['side_dish'])
        info = sidesdetails(response.query_result.parameters['side_dish'])
        print("item info is ", info)
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                          params={"access_token": ACCESS_TOKEN},
                          data=json.dumps({
                              "recipient": {
                                  "id": sender
                              },
                              "message": {
                                  "attachment": {
                                      "type": "template",
                                      "payload": {
                                          "template_type": "generic",
                                          "elements": [
                                              {
                                                  "title": (info[0] + " : $" + str(info[1])),
                                                  "image_url": info[3],
                                                  "subtitle": (info[2] + " The price of the sides is " + str(info[1])),
                                                  "default_action": {
                                                      "type": "web_url",
                                                      "url": info[3],
                                                      "webview_height_ratio": "tall",
                                                  },
                                                  "buttons": [
                                                      {
                                                          "type": "postback",
                                                          "title": "Order now",
                                                          "payload": info[0]
                                                      }
                                                  ]
                                              }
                                          ]
                                      }
                                  }
                              }
                          }),
                          headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print(r.text)

    elif intentofDF == "postback_order":
        postbackfoodorder = str(int(response.query_result.parameters['number']))
        print("postbackfoodorder before adding food is: ", postbackfoodorder)
        postbackfoodorder = postbackfoodorder + " " + postbackfood
        print("postbackfoodorder before complexq: ", postbackfoodorder)
        # postbackspeech = complexq(postbackfoodorder,False)
        postbackspeech = complexq(postbackfoodorder)
        reply(sender, postbackspeech)

    elif intentofDF == "postback_order - yes":
        processedorder = totalprice()
        reply(sender, str(processedorder))
        postbackspeech = ""
        postbackfoodorder = ""
        postbackfood = ""
        session.__del__()

    elif intentofDF == "postback_order - no":
        reply(sender, "Can you repeat your order to me again? Thanks!")
        postbackspeech = ""
        postbackfoodorder = ""
        postbackfood = ""

    elif message == "Get started":
        r = requests.post("https://graph.facebook.com/v2.6/me/messages",
                          params={"access_token": ACCESS_TOKEN},
                          data=json.dumps({
                              "recipient": {
                                  "id": sender
                              },
                              "message": {
                                        "text": "What do you wish to eat today? You can browse our menu with the button below."
                                                " Alternatively, you can tell me the food/beverage that you want, with the quantity behind it. "
                                                "For example, 2 char kway teow and 1 milk tea",
                                        "quick_replies": [
                                          {
                                            "content_type": "text",
                                            "title": "Menu",
                                            "payload": "Menu"
                                          }
                                        ]
                                      }
                          }),
                          headers={'Content-type': 'application/json'})
        if r.status_code != requests.codes.ok:
            print(r.text)

    return 'OK'



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
