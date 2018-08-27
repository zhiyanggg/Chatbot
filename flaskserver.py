import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response
from complexquery import *
from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import pprint
import mysql
from loop1 import food
# Flask app should start in global layout
app = Flask(__name__)


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
        # print("type: ", type(json.dumps(result)))
        return result

    if intentofDF == "Complexquery - yes":
        __DEBUG__ = True
        # engine = create_engine('mysql+mysqlconnector://zy:zy123456@localhost/canteena_fnb?charset=utf8',
        #                        encoding='utf8')
        engine = create_engine('mysql+mysqlconnector://zy:zy123456@localhost/canteena_fnb', pool_recycle=3600)
        print("logon to mysql")
        Session = sessionmaker(bind=engine)
        s = Session()
        print("session created")
        retStr = "Total price: S$"
        totalprice = 0.0

        for idx, item in enumerate(food):
            query = s.query(Food.fprice).filter(Food.fname.in_([foods[0]]))
            result = query.first()
            unit_price = 3.0
            if result:
                unit_price = float(result[0])
                if (__DEBUG__):
                    print("Checking price of your order")
                    pprint.pprint(result[0])

            noItems = 1.0
            if (idx < len(units)):
                numberStr = ""
                if (units[idx] != None):
                    numberStr = str(units[idx]).replace("\"", "")
                noItems = float(numberStr)
            totalprice = totalprice + unit_price * noItems

        if (__DEBUG__):
            print("Total price: " + str(totalprice))

        result1 = retStr + str(totalprice)
        return result1






if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')