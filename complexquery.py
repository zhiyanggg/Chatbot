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
from spacy_api import LocalClient
from spacy_api import api
from spacy_api import Client
import json

cachedStopWords = open("C:/Users/Asus-Laptop/Desktop/stopwords.txt", "r")
cachedStopWords = cachedStopWords.read()

foodorder = []

class Orderitem():

    def __init__(self, quantity=None, name=None):
        self.size = None

        if quantity == "0" or quantity == "zero" or quantity == "Zero":
            print("You need to input a quantity for the item " + name)


def cleantext(s):   # remove stop words, multiple spaces, special characters and punctuations
    s = s.lower()
    remove = regex.compile(u'[\p{C}|\p{M}|\p{P}|\p{S}|\p{Z}\pp{D}]+', regex.UNICODE)
    s = remove.sub(u" ", s).strip()
    s = spellingchecker(s)
    nlp = api.get_nlp(model="en_core_web_md", embeddings_path="en_google")

    # nlp = ('en_core_web_md')
    # nlp.remove_pipe('parser')
    document = nlp(s)
    # for token in document:
    #     print(token, token.lemma_)
    s = ' '.join([token.lemma_ for token in document])
    # print(s)# after lemmatization
    newstring = ""
    for word in s.split():
        if word == "fry":
            word = "fries"
        newstring += word
        newstring += " "
    s = newstring
    # print(newstring)# after attempt
    s = ' '.join([word for word in s.split() if word not in cachedStopWords])
    print(s) # after removing stopwords
    # print('Entities', [(ent.text, ent.label_) for ent in document.ents])
    # count = 0
    # for z in document:
    #     if z.ent_type_ == 'CARDINAL':
    #         a = Orderitem()
    #         a.quantity = z.text
    #         # if document[count+1].text == "small" or document[count+1].text == "medium"\
    #         #         or document[count+1].text == "large" or document[count+1].text == "extra-large" \
    #         #         or document[count + 1].text == "tiny" or document[count+1].text == "regular" \
    #         #         or document[count + 1].text == "big" or document[count+1].text == "giant" \
    #         #         or document[count + 1].text == "enormous":
    #         #     a.size = document[count+1].text
    #         # else:
    #         #     a.size = None
    #         # print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in document])
    #         # print(document[count].rights)
    #         foodorder.append(a)
    #         count = count + 1
    # for obj in foodorder:
    #     print(obj.quantity)
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
def main(model=None, new_model_name='food', output_dir="C:/Users/Asus-Laptop/Desktop", n_iter=20):
    # """Set up the pipeline and entity recognizer, and train the new entity."""
    # if model is not None:
    #     nlp = spacy.load(model)  # load existing spaCy model
    #     print("Loaded model '%s'" % model)
    # else:
    #     nlp = spacy.blank('en')  # create blank Language class
    #     print("Created blank 'en' model")
    # # Add entity recognizer to model if it's not in the pipeline
    # # nlp.create_pipe works for built-ins that are registered with spaCy
    # if 'ner' not in nlp.pipe_names:
    #     ner = nlp.create_pipe('ner')
    #     nlp.add_pipe(ner)
    # # otherwise, get it, so we can add labels to it
    # else:
    #     ner = nlp.get_pipe('ner')
    #
    # ner.add_label('DRINKS')  # add new entity label to entity recognizer
    # ner.add_label('SIDES')  # add new entity label to entity recognizer
    # ner.add_label('FOOD')   # add new entity label to entity recognizer
    # ner.add_label('SIZE')   # add new entity label to entity recognizer
    # ner.add_label('QUANTITY')   # add new entity label to entity recognizer
    # # print("added labels")
    # if model is None:
    #     optimizer = nlp.begin_training()
    #     # print("beginning training")
    # else:
    #     # Note that 'begin_training' initializes the models, so it'll zero out
    #     # existing entity types.
    #     optimizer = nlp.entity.create_optimizer()
    #
    # # get names of other pipes to disable them during training
    # other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
    # with nlp.disable_pipes(*other_pipes):  # only train NER
    #     for itn in range(n_iter):
    #         random.shuffle(TRAIN_DATA)
    #         # print("finish shuffling")
    #         losses = {}
    #         for text, annotations in tqdm(TRAIN_DATA):
    #             nlp.update([text],  # batch of texts
    #                        [annotations],  # batch of annotations
    #                        sgd=optimizer,  # callable to update weights
    #                        drop=0.35,  # make it harder to memorise data
    #                        losses=losses)
    #         print(losses)
    #         print("losses fault")
    #
    # # save model to output directory
    # if output_dir is not None:
    #     output_dir = Path(output_dir)
    #     if not output_dir.exists():
    #         output_dir.mkdir()
    #     nlp.meta['name'] = new_model_name  # rename model
    #     nlp.to_disk(output_dir)
    #     print("Saved model to", output_dir)


    # test the saved model
    print("initiating timer for test cases")
    start1 = time.time()
    test_text = 'i want 10 stiks of large oyster omelette    3 small frys 4 lage briyani 5 smal soup 6 meium char kay tew' # works for space, stopwords and punctuations
    test_text = cleantext(test_text)
    # print("Loading from", output_dir)
    # nlp = spacy.load(output_dir)
    spacy_client = Client()
    nlp = api.get_nlp(model=output_dir)
    doc2 = nlp(test_text)
    print("testing with space")
    # print('Entities', [(ent.text, ent.label_) for ent in doc2.ents])
    print(spacy_client.testfunc(doc2))
    end1 = time.time()
    print(end1-start1)

    test_text1 = 'i want 3 sticks of satay,，。@!@#$ 4 biryani， 5 pasta, 6 oyster omelette 7 mash potato 8 soup 9 milk tea'
    # works for space, stopwords and punctuations
    start2 = time.time()
    test_text1 = cleantext(test_text1)
    doc3 = nlp(test_text1)
    print("testing with punctuations and special characters")
    # print('Entities', [(ent.text, ent.label_) for ent in doc3.ents])
    print(spacy_client.testfunc(doc3))
    end2 = time.time()
    print(end2 - start2)


    test_text2 = 'i want 3 sticks of satay, 4 fries and 3 cups of coffee and 4 portion of toast cubes'  # works for space, stopwords and punctuations
    start3 = time.time()
    test_text2 = cleantext(test_text2)
    doc4 = nlp(test_text2)
    print("testing with stopwords")
    # print('Entities', [(ent.text, ent.label_) for ent in doc4.ents])
    print(spacy_client.testfunc(doc4))
    end3 = time.time()
    print(end3 - start3)

if __name__ == '__main__':
    plac.call(main)