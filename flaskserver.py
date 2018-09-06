import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
from complexquery import *
from loop1 import food
import re


# Flask app should start in global layout
app = Flask(__name__)

speech = ""

@app.route('/', methods=['POST'])
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
    global speech
    intentofDF = req.get("queryResult").get("intent").get("displayName")
    if intentofDF == "Complexquery":
        speech = complexq()
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
        return result

    if intentofDF == "Complexquery - yes":
        processedorder = totalprice("C:/Users/Asus-Laptop/Desktop", speech)
        result = {
            "fulfillmentText": processedorder,
            # "source": "facebook",
            "fulfillmentMessages": [
                {
                    "platform": "FACEBOOK",
                    "text": {
                        "text": [
                            "The total price for your order is $", processedorder
                        ]
                    }
                }
            ],
        }
        return result

    if intentofDF == "list_drink":
        result = {
            "fulfillmentMessages": [
                {
                    "platform": "FACEBOOK",
                    "text": {
                        "text": [
                            "We have the following sides: ", drinkslist()
                        ]
                    }
                }
            ],
        }
        return result

    if intentofDF == "list_side_dishes":
        result = {
            "fulfillmentMessages": [
                {
                    "platform": "FACEBOOK",
                    "text": {
                        "text": [
                            "We have the following sides: ", sideslist()
                        ]
                    }
                }
            ],
        }
        return result

    if intentofDF == "list_food_by_cuisine":
        result = {
            "fulfillmentMessages": [
                {
                    "platform": "FACEBOOK",
                    "text": {
                        "text": [
                            "We have the following food: ", foodlist()
                        ]
                    }
                }
            ],
        }
        return result


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')