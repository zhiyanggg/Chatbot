from __future__ import unicode_literals, print_function

import plac
import random
from pathlib import Path
import spacy
from loop1 import *
import regex
from symspell import *
import time
from tqdm import tqdm
import json
from flask import request
import mysql
import mysql.connector

config = {
    'user': 'b521de1b9b742d',
    'password': 'c80285f8',
    'host': 'us-cdbr-iron-east-01.cleardb.net',
    'database': 'heroku_b719ec770e665f0',
    'raise_on_warnings': True,
	'connect_timeout': 1800,
}

nlp = spacy.load("/app/en_core_web_sm")
print("loaded en_core_web_sm model succeeded")

nlp1 = spacy.load("/app")
print("loaded self-trained model succeeded")

cachedStopWords = open("/app/stopwords.txt", "r")
cachedStopWords = cachedStopWords.read()
numbers = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
foodordered = []
drinksordered = []
sidesordered = []
cnx = mysql.connector.connect(**config)
print("logon to mysql")
cursor = cnx.cursor(buffered=True)

def connecttomysql():
    global cursor, cnx
    cnx = mysql.connector.connect(**config)
    print("logon to mysql")
    cursor = cnx.cursor(buffered=True)


def cleantext(s):   # remove stop words, multiple spaces, special characters and punctuations
    s = s.lower()
    remove = regex.compile(u'[\p{C}|\p{M}|\p{P}|\p{S}|\p{Z}\pp{D}]+', regex.UNICODE)
    s = remove.sub(u" ", s).strip()
    newstring1 = ""

    for word1 in s.split():
        if word1 in numbers.keys():
            word1 = str(numbers[word1])
            newstring1 += word1
            newstring1 += " "
        else:
            newstring1 += word1
            newstring1 += " "

    s = newstring1

    print("this is newstring ", s)
    s = spellingchecker(s)
    # nlp = ('en_core_web_md')
    # nlp.remove_pipe('parser')
    document = nlp(s)
    print("created doc for en model")

    s = ""

    for token in document:
        if token.text == "fries":
            s += token.text
            s += " "
        else:
            s += token.lemma_
            s += " "

    # for ent in document.ents:
    #     print(ent.text, ent.label_)

    print(s)# after lemmatization
    newstring = ""
    for word in s.split():
        if word == "frys":
            word = "fries"

        elif word == "fry":
            word = "fried"

        newstring += word
        newstring += " "

    s = newstring
    print(newstring)# after attempt
    s = ' '.join([word for word in s.split() if word not in cachedStopWords])
    print(s)# after removing stopwords
    return s

# test_text2 = 'i want 3 sticks of satay, 4 fries and 3 cups of coffee'
# test_text1 = 'i want 3 sticks of satay,!@# 4 biryani， 5 pasta,$%^&*()_ 6                   oyster omelette'
# print(cleantext(test_text2))

# training data
# Note: If you're using an existing model, make sure to mix in examples of
# other entity types that spaCy correctly recognized before. Otherwise, your
# model might learn the new type, but "forget" what it previously knew.
# https://explosion.ai/blog/pseudo-rehearsal-catastrophic-forgetting

TRAIN_DATA = foodtraining()
# print(TRAIN_DATA)

@plac.annotations(
    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
    new_model_name=("New model name for model meta.", "option", "nm", str),
    output_dir=("Optional output directory", "option", "o", Path),
    n_iter=("Number of training iterations", "option", "n", int))
def trainnewmodel(model=None, new_model_name='food', output_dir="/app", n_iter=20):
    # """Set up the pipeline and entity recognizer, and train the new entity."""
    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model
        print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class
        print("Created blank 'en' model")
    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    ner.add_label('DRINKS')  # add new entity label to entity recognizer
    ner.add_label('SIDES')  # add new entity label to entity recognizer
    ner.add_label('FOOD')   # add new entity label to entity recognizer
    ner.add_label('SIZE')   # add new entity label to entity recognizer
    ner.add_label('QUANTITY')   # add new entity label to entity recognizer
    # print("added labels")
    if model is None:
        optimizer = nlp.begin_training()
        # print("beginning training")
    else:
        # Note that 'begin_training' initializes the models, so it'll zero out
        # existing entity types.
        optimizer = nlp.entity.create_optimizer()

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    with nlp.disable_pipes(*other_pipes):  # only train NER
        for itn in range(n_iter):
            random.shuffle(TRAIN_DATA)
            # print("finish shuffling")
            losses = {}
            for text, annotations in tqdm(TRAIN_DATA):
                nlp.update([text],  # batch of texts
                           [annotations],  # batch of annotations
                           sgd=optimizer,  # callable to update weights
                           drop=0.35,  # make it harder to memorise data
                           losses=losses)
            print(losses)
            print("losses fault")

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)


    # # test the saved model
    # Uncomment the following section below if you wish to deploy this script on Dialogflow
    ## This is the start of the section that contains testing samples
    # print("initiating timer for test cases")
    # start1 = time.time()
    # test_text = '9 stiks of large oyster omelette    three small frys four lage briyani 5 smal soup six meium char kay tew' # works for space, stopwords and punctuations
    # # test_text = "nine large chickwen rice        3 small frys 4 lage briyani 6 smal soup 6 medim char kay tew "
    # test_text = cleantext(test_text)
    # # print("Loading from", output_dir)
    # # nlp = spacy.load(output_dir)
    # spacy_client = Client()
    # nlp = api.get_nlp(model=output_dir)
    # doc2 = nlp(test_text)
    # print("testing with space")
    # # print('Entities', [(ent.text, ent.label_) for ent in doc2.ents])
    # print(spacy_client.testfunc(doc2))
    # end1 = time.time()
    # print(end1-start1)
    #
    # test_text1 = 'i want 3 sticks of satay,，。@!@#$ 4 biryani， 5 pasta, 6 oyster omelette 7 mash potato 8 soup 9 milk tea'
    # # works for space, stopwords and punctuations
    # start2 = time.time()
    # test_text1 = cleantext(test_text1)
    # doc3 = nlp(test_text1)
    # print("testing with punctuations and special characters")
    # # print('Entities', [(ent.text, ent.label_) for ent in doc3.ents])
    # print(spacy_client.testfunc(doc3))
    # end2 = time.time()
    # print(end2 - start2)
    #
    #
    # test_text2 = 'i want 3 sticks of satay, 4 fries and 3 cups of coffee and 4 portion of toast cubes'  # works for space, stopwords and punctuations
    # start3 = time.time()
    # test_text2 = cleantext(test_text2)
    # doc4 = nlp(test_text2)
    # print("testing with stopwords")
    # # print('Entities', [(ent.text, ent.label_) for ent in doc4.ents])
    # print(spacy_client.testfunc(doc4))
    # end3 = time.time()
    # print(end3 - start3)
    # ## This is the end of the section that contains testing samples


def complexq(query_text):
    doc4 = nlp1(query_text)
    print("created doc for food model")
    result = "You wish to order "
    quantity = []
    count = 0
    totalcount = len(doc4.ents)
    global foodordered, drinksordered, sidesordered
    foodordered.clear()
    drinksordered.clear()
    sidesordered.clear()

    for ent in doc4.ents:
        if count == totalcount-3 and count != 0 and ent.label_ == "QUANTITY":
            result += " and "

        if count == totalcount - 2 and count != 0 and ent.label_ == "QUANTITY":
            result += " and "


        if (ent.label_) == "QUANTITY":
            result += ent.text
            quantity.clear()
            quantity.append(ent.text)
            result += " "
            count = count + 1
            continue

        if (ent.label_) == "FOOD":
            if quantity:
                foodordered.append(quantity[0])
                foodordered.append(ent.text)
                result += ent.text
                if (count == totalcount - 2 and count != 0) or (count == totalcount-3 and count != 0):
                    count = count + 1
                    continue
                else:
                    result += " "
                    count = count + 1
                    continue

            else:
                # print("Please input the quantity for your food,", ent.text, ": ")
                # quantityoffood = input()
                # foodordered.append(quantityoffood)
                # foodordered.append(ent.text)
                # result += ent.text
                # # result += ", "
                # count = count + 1
                continue

        if (ent.label_) == "DRINKS":
            if quantity:
                drinksordered.append(quantity[0])
                drinksordered.append(ent.text)
                result += ent.text
                if (count == totalcount - 2 and count != 0) or (count == totalcount - 3 and count != 0):
                    count = count + 1
                    continue
                else:
                    result += " "
                    count = count + 1
                    continue

            else:
                # print("Please input the quantity for your drinks,", ent.text, ": ")
                # quantityofdrinks = input()
                # drinksordered.append(quantityofdrinks)
                # drinksordered.append(ent.text)
                # result += ent.text
                # # result += ", "
                # count = count + 1
                continue

        if (ent.label_) == "SIDES":
            if quantity:
                sidesordered.append(quantity[0])
                sidesordered.append(ent.text)
                result += ent.text
                if (count == totalcount - 2 and count != 0) or (count == totalcount - 3 and count != 0):
                    count = count + 1
                    continue
                else:
                    result += " "
                    count = count + 1
                    continue

            else:
                # print("Please input the quantity for your sides,", ent.text, ": ")
                # quantityofsides = input()
                # sidesordered.append(quantityofsides)
                # sidesordered.append(ent.text)
                # result += ent.text
                # # result += ", "
                # count = count + 1
                continue


        else:
        #     result += ent.text
        #     result += ", "
        #     count = count + 1
             continue


    print('Entities', [(ent.text, ent.label_) for ent in doc4.ents])
    # result = (spacy_client.testfunc(doc4))
    return result


def totalprice():
    totalresponse = ""
    total = float(0)
    if not cnx.is_connected():
        connecttomysql()

    for i in range(len(sidesordered)):
        print("this is the sides ordered", sidesordered[i])
        sqlquery = ""

        if len(sidesordered) == 0:
            break

        if sidesordered[i].isnumeric():
            continue

        else:
            sqlquery += sidesordered[i]
            query = "SELECT * FROM sides WHERE sname = %s"
            cursor.execute(query, (sqlquery,))
            result = cursor.fetchone()
            sidesprice = float(sidesordered[i-1]) * result[1]
            sidesname = result[0]
            total += sidesprice
            totalresponse += (sidesname + " ($" + str(float(result[1])) + ") " + " X " + str(int(sidesordered[i-1])) + " = $" + str(round(sidesprice, 2)))
            totalresponse += "\u000A"


    for i in range(len(drinksordered)):
        print("this is the drinks ordered", drinksordered[i])
        sqlquery = ""

        if len(drinksordered) == 0:
            break

        if drinksordered[i].isnumeric():
            continue

        else:
            sqlquery += drinksordered[i]
            query = "SELECT * FROM drinks WHERE dname = %s"
            cursor.execute(query, (sqlquery,))
            result = cursor.fetchone()
            drinksprice = float(drinksordered[i-1]) * result[1]
            drinksname = result[0]
            total += drinksprice
            totalresponse += (drinksname + " ($" + str(float(result[1])) + ") " + " X " + str(int(drinksordered[i-1])) + " = $" + str(round(drinksprice, 2)))
            totalresponse += "\u000A"

    for i in range(len(foodordered)):
        print("this is the food ordered", foodordered[i])
        sqlquery = ""

        if len(foodordered) == 0:
            break

        if foodordered[i].isnumeric():
            continue

        else:
            sqlquery += foodordered[i]
            query = "SELECT * FROM food WHERE fname = %s"
            cursor.execute(query, (sqlquery,))
            result = cursor.fetchone()
            foodprice = float(foodordered[i-1]) * result[1]
            foodname = result[0]
            total += foodprice
            totalresponse += (foodname + " ($" + str(float(result[1])) + ") " + " X " + str(int(foodordered[i-1])) + " = $" + str(round(foodprice, 2)))
            totalresponse += "\u000A"


    totalresponse += "----------------------------"
    totalresponse += "\u000A"
    totalresponse += ("Total price for today's meal is $" + str(total))
    print("this is the total price, ", total)
    print(totalresponse)
    return totalresponse


def foodlist():
    foodlist = ""
    query = "SELECT fname FROM food"
    cursor.execute(query)
    for row in cursor:
        foodlist += row[0]
        foodlist += "\u000A"
    return foodlist

def sideslist():
    sideslist = ""
    query = "SELECT sname FROM sides"
    cursor.execute(query)
    for row in cursor:
        sideslist += row[0]
        sideslist += "\u000A"
    return sideslist

def drinkslist():
    drinkslist = ""
    query = "SELECT dname FROM drinks"
    cursor.execute(query)
    for row in cursor:
        drinkslist += row[0]
        drinkslist += "\u000A"
    return drinkslist

def drinksdetails(s):
    drinksdetailslist = []
    sqlquery = s
    query = "SELECT * FROM drinks WHERE dname = %s"
    cursor.execute(query, (sqlquery,))
    for col in cursor.fetchone():
        print(col)
        drinksdetailslist.append(col)
    return drinksdetailslist

def sidesdetails(s):
    sidesdetailslist = []
    sqlquery = s
    query = "SELECT * FROM sides WHERE sname = %s"
    cursor.execute(query, (sqlquery,))
    for col in cursor.fetchone():
        print(col)
        sidesdetailslist.append(col)
    return sidesdetailslist


def fooddetails(s):
    fooddetailslist = []
    sqlquery = s
    print("sqlquery is", sqlquery)
    print("type of sqlquery is ", type(sqlquery))
    query = "SELECT * FROM food WHERE fname = %s"
    cursor.execute(query, (sqlquery,))
    for col in cursor.fetchone():
        print(col)
        fooddetailslist.append(col)
    return fooddetailslist

# if __name__ == '__main__':
#     plac.call(main)