# NTU Foodchatbot

Foodchatbot for NTU NorthSpine Canteen A

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. Do ensure you navigate to the "for download" branch before you start downloading the files.

### Prerequisites
You will need to create a account in Dialogflow and Facebook so that you can test the script at the end. 
```
Python 2.7/3 and above
Ngrok
Dialogflow
Facebook 
```

### Installing

First, you will need to have the following libraries in Python:


```
plac
random
pathlib
spacy
symSpell
regex
time
tqdm
spacy_api
json
flask

```


## Building the model
After installing the libraries above, you will need to change the output directory(variable name is, "output_dir") in the complexquery.py script to your own directory which you wish to save the trained spacy model.
You will need to run the main function in complexquery.py. Do take note of putting all the downloaded files within the same directory so as to facilitate the importing of files. 
Once you run the function, just sit back and relax as the building of model takes a few hours to train. 

## Deployment

After you are done with training for the model, you can test how complex queries are processed with complexquery.py. I have provided 3 test cases for the following scenarios. 
1) Multiple spaces with misspelled words and stopwords in a query
2) Multiple spaces with stopwords, special symbols and punctuations in a query
3) Stopwords 

Once you get a hang of how everything works, you can test the script online on Dialogflow. Before we do that, there are some things you need to do first.

Firstly, you will need to change the name of the "main" function in complexquery.py to this new name, "complexq". Next, you will need to find the following 2 lines of code in the same python script(complexquery.py) and coment them out.

```
if __name__ == '__main__':
    plac.call(main)
```

Once you are done with that, you can start running the following commands below sequentially in separate command prompt/terminal to test everything out. 

For the first command prompt window,
```
spacy serve
```
This will run the server to load the model. The next step would be to run the following command below in a new command prompt window.

```
ngrok http 5000
```

Lastly, run the flaskserver.py script using a new command prompt window so that you can create your own flask server. This flask server will be useful  You can monitor the post and get requests in this window 
should you need to debug any errors.

Deployment does not stop here as you will still need to copy and paste the https url link in the dialogflow fulfillment section. Upon navigated to this section, paste the ngrok https
 url link in the "URL" box under "Webhook". Next, create a intent named "Complexquery"  with the following training phrases below for testing. 
 "2 chicken rice 5 kopi 1 pasta and 1 bubble tea"
 "1 oyster omelette 4 kopi and 1 pasta"
 "1 char kway teow 3 kopi"
 
Do remember to annotate the entities in the training phrases with the pictures seen in the email i have sent you. Also, please enable the webhook settings in your dialogflow.
 
 Last by not least, you can proceed to test the webhooking out with the console on your right!
## Authors

* **Lim Zhi Yang** 
