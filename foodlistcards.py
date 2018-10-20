
import requests
import json


def foodpage1(accesstoken, sender):
    ACCESS_TOKEN = accesstoken
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
                                          "title": "aglio olio chicken chop , $ 5.0",
                                          "image_url": "http://4.bp.blogspot.com/-7UwaNrcWZqI/TrFHDzzFHzI/AAAAAAAAKd0/UtaHvJhV0QE/s1600/Grilled+Chicken+with+Pasta+Aglio+E+Olio+October+31st%252C+2011.jpg",
                                          "subtitle": "This dish is made by lightly sauteeing sliced, minced, or pressed garlic in olive oil, sometimes with the addition of dried red chili flakes, and tossing with spaghetti topped with chicken chop",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "aglio olio chicken chop"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "aglio olio chicken cutlet , $ 5.0",
                                          "image_url": "http://cookdiary.net/wp-content/uploads/images/Chicken-and-Noodles.jpg",
                                          "subtitle": "This dish is made by lightly sauteeing sliced, minced, or pressed garlic in olive oil, sometimes with the addition of dried red chili flakes, and tossing with spaghetti topped with chicken cutlet.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "aglio olio chicken cutlet"
                                              }
                                          ]
                                      },
                                      {

                                          "title": "bak chor mee , $ 4.0",
                                          "image_url": "https://mtc1-dydfxmh.netdna-ssl.com/wp-content/uploads/2017/03/P1040774-1300x867.jpg",
                                          "subtitle": "Bak Chor Mee (肉脞面) literally means “minced meat and noodles” in the Teochew dialect.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "bak chor mee"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "bak kut teh , $ 5.0",
                                          "image_url": "https://i.hungrygowhere.com/business/42/60/12/00/a2-bkt_594x0_crop_594x372_0668d8d8a6.jpg",
                                          "subtitle": "Singapore Teochew Bak Kut Teh is a version of pork ribs tea with a clear garlicky and peppery broth. Only a few ingredients and very easy to prepare.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "bak kut teh"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "bee hoon , $ 1.2",
                                        "image_url" : "https://s3-ap-southeast-1.amazonaws.com/afc-prod/thumbnails/standard_mobile/5415/0286/1193/tn-HFM-Braised-Pig-Trotter-Bee-Hoon.jpg",
                                        "subtitle" : "Rice vermicelli are a thin form of rice noodles. They are sometimes referred to as rice noodles, rice sticks, or bee hoon, but they should not be confused with cellophane noodles which are a different Asian type of vermicelli made from mung bean starch or",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "bee hoon"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "beef , $ 4.0",
                                        "image_url" : "https://www-cuisinesolutions-com-production.s3.amazonaws.com/media/products/slicedbeef/original.jpg",
                                        "subtitle" : "Beef is the culinary name for meat from cattle, particularly skeletal muscle.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "beef"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "biryani , $ 4.0",
                                        "image_url" : "http://www.ndtv.com/cooks/images/mutton-biryani-new.jpg",
                                        "subtitle" : "Biryani, also known as biriyani, biriani, birani or briyani, 'spicy rice' is a South Asian mixed rice dish with its origins among the Muslims of the Indian subcontinent.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "biryani"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "bun bo hue , $ 5.0",
                                        "image_url" : "https://media.foody.vn/res/g65/642530/prof/s/foody-mobile-ba-thu-jpg-537-636255976625248994.jpg",
                                        "subtitle" : "Bún bò Huế or bún bò is a popular Vietnamese soup containing rice vermicelli (bún) and beef (bò). Huế is a city in central Vietnam associated with the cooking style of the former royal court. The dish is greatly admired for its balance of spicy, sour, sal",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "bun bo hue"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "char kway teow , $ 3.0",
                                        "image_url" : "https://4scoin37ye-flywheel.netdna-ssl.com/wp-content/uploads/2014/03/charkwayteow2.jpg",
                                        "subtitle" : "Char kway teow, literally 'stir-fried ricecake strips', is a popular noodle dish in Malaysia, Singapore, Brunei and Indonesia. The dish is considered a national favourite in Malaysia and Singapore",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "char kway teow"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "More food in the next page!",
                                          "image_url": "https://i5.walmartimages.com/dfw/4ff9c6c9-28f7/k2-_327d5c10-c756-40e0-90cf-d071d67b05a5.v2.jpg",
                                        "buttons":[
                                              {
                                                  "type": "postback",
                                                  "title": "View More food",
                                                  "payload": "View More food page 2"
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

def foodpage2(accesstoken, sender):
    ACCESS_TOKEN = accesstoken
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
                                        "title" : "chicken burger , $ 3.0",
                                        "image_url" : "https://www.chicken.ca/assets/RecipePhotos/_resampled/FillWyI3MjAiLCI2MDAiXQ/Moist-Chicken-Burgers.jpg",
                                        "subtitle" : "A hot sandwich made of a patty of chicken in a bun, often with other ingredients.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "chicken burger"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "chicken rice , $ 3.0",
                                        "image_url" : "https://i.kinja-img.com/gawker-media/image/upload/s--TQiCqzhq--/c_scale,f_auto,fl_progressive,q_80,w_800/d9jqrqz6srm6z31cnnm4.jpg",
                                        "subtitle" : "Hainanese chicken rice is a dish adapted from early Chinese immigrants originally from Hainan province in southern China.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "chicken rice"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "wanton mee , $ 3.0",
                                        "image_url" : "https://c4.staticflickr.com/8/7386/27790732171_558d9ac9d3_b.jpg",
                                        "subtitle" : "Wonton noodles is a Cantonese noodle dish which is popular in Guangzhou, Hong Kong, Malaysia, Singapore and Thailand.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "wanton mee"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "crabs , $ 20.0",
                                          "image_url": "https://www.thespruceeats.com/thmb/iR3fKo4lRqANDPkfUsmPaTl7qxg=/4738x2533/filters:no_upscale():max_bytes(150000):strip_icc()/close-up-of-crab-gravy-served-on-table-677147575-588b52995f9b5874ee1af765.jpg",
                                          "subtitle": "Chilli crab is a popular seafood dish among locals and foreigners in Singapore, and consists of mud crabs deep-fried in a sweet, savoury and spicy gravy.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "crabs"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "curry fish head , $ 18.0",
                                        "image_url" : "https://farm5.staticflickr.com/4233/35800092885_902a64e85b_o.jpg",
                                        "subtitle" : "Fish head curry is a dish in Singaporean and Malaysian cuisine with Indian and Chinese origins. The head of a red snapper is semi-stewed in a Kerala-style curry with assorted vegetables such as okra and eggplants.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "bee hoon"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "dim sum , $ 1.2",
                                        "image_url" : "https://dynaimage.cdn.cnn.com/cnn/q_auto,w_900,c_fill,g_auto,h_506,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F160325033254-hk-dim-sum-fook-lam-moon.jpg",
                                        "subtitle" : "Dim sum is a style of Chinese cuisine prepared as small bite-sized portions of food served in small steamer baskets or on small plates. Dim sum dishes are usually served with tea and together form a full tea brunch. Dim sum traditionally are served as ful",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "dim sum"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "spaghetti with sausage , $ 5.0",
                                        "image_url" : "https://img.taste.com.au/pSKAAN57/w720-h480-cfill-q80/taste/2016/11/mushroom-and-ham-spaghetti-25701-1.jpeg",
                                        "subtitle" : "Delicious pieces of ham add a meaty touch to this hearty pasta dish.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "spaghetti with sausage"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "fish burger , $ 3.0",
                                        "image_url" : "https://img.taste.com.au/rcvt-lIB/taste/2016/11/fish-burgers-with-tartare-sauce-108735-1.jpeg",
                                        "subtitle" : "A hot sandwich made of a fish fillet in a bun, often with other ingredients.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "fish burger"
                                              }
                                          ]
                                      },
                                      {

                                        "title" : "fish n chips , $ 5.0",
                                        "image_url" : "https://cdn-triplem.scadigital.io/media/9052/fishnchips.jpg?preset=MainImage",
                                        "subtitle" : "Fish and chips is a hot dish of English origin consisting of fried battered fish and hot potato chips. It is a common take-away food and an early example of culinary fusion.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "fish n chips"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "More food in the next page!",
                                          "image_url": "https://i5.walmartimages.com/dfw/4ff9c6c9-28f7/k2-_327d5c10-c756-40e0-90cf-d071d67b05a5.v2.jpg",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "View More food",
                                                  "payload": "View More food page 3"
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

def foodpage3(accesstoken, sender):
    ACCESS_TOKEN = accesstoken
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
                                        "title" : "fried carrot cake , $ 3.0",
                                        "image_url" : "http://www.singaporebestfoods.com/wp-content/uploads/2017/09/Yuan-Cheng-Fried-Carrot-Cake-3.jpg",
                                        "subtitle" : "Fried carrot cake, or chai tow kway in the Teochew dialect, consists of cubes of radish cake stir-fried with garlic, eggs and preserved radish.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "fried carrot cake"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "fried hokkien mee , $ 5.0",
                                        "image_url" : "https://mtc1-dydfxmh.netdna-ssl.com/wp-content/uploads/2016/12/16069838051_c75eb4dd99_o-1300x867.jpg",
                                        "subtitle" : "Hokkien mee is a dish in Malaysian and Singaporean cuisine that has its origins in the cuisine of China's Fujian province.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "fried hokkien mee"
                                              }
                                          ]
                                      },
                                      {

                                        "title" : "hokkien char mee , $ 4.0",
                                        "image_url" : "http://p1.meituan.net/poirichness/menu_6597338_58965842.jpg%40249w_249h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20",
                                        "subtitle" : "福建炒麵) is served in Kuala Lumpur and the surrounding region. It is a dish of thick yellow noodles braised in thick dark soy sauce with pork, squid, fish cake and cabbage as the main ingredients and cubes of pork fat fried until crispy (sometimes pork liver",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "hokkien char mee"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "hokkien prawn mee , $ 4.0",
                                        "image_url" : "https://rasamalaysia.com/wp-content/uploads/2011/01/hokkien-mee-8.jpg",
                                        "subtitle" : "Hokkien Prawn Mee, also affectionately known as 福建蝦麵, is another favourite of every local in Singapore.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "hokkien prawn mee"
                                              }
                                          ]
                                      },
                                      {

                                          "title": "laksa , $ 4.0",
                                          "image_url": "https://makanzeit.files.wordpress.com/2018/02/sungei_road_laksa_resize.png",
                                          "subtitle": "Laksa consists of rice noodles or rice vermicelli with chicken, prawn or fish, served in spicy soup based on either rich and spicy curry coconut milk or on sour asam.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "laksa"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "mee siam , $ 4.0",
                                        "image_url" : "http://mayakitchenette.com/wp-content/uploads/2014/07/mee-siam-recipe-3.jpg",
                                        "subtitle" : "Mee siam, which means 'Siamese noodle' in Malay, is a dish of thin rice vermicelli popular in Singapore and Malaysia.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "mee siam"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "nasi lemak , $ 3.0",
                                        "image_url" : "https://d1alt1wkdk73qo.cloudfront.net/images/guide/6abb55670f06cebacdc5023d11367153/640x478_ac.jpg",
                                        "subtitle" : "Nasi lemak is a Malay fragrant rice dish cooked in coconut milk and pandan leaf. It is commonly found in Malaysia, where it is considered the national dish; it is also popular in neighbouring areas such as Singapore; Brunei, and Southern Thailand.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "nasi lemak"
                                              }
                                          ]
                                      },
                                      {

                                        "title" : "noodle , $ 2.0",
                                        "image_url" : "https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Mama_instant_noodle_block.jpg/1200px-Mama_instant_noodle_block.jpg",
                                        "subtitle" : "A very thin, long strip of pasta or a similar flour paste, eaten with a sauce or in a soup.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "noodle"
                                              }
                                          ]
                                      },
                                      {

                                        "title" : "oyster omelette , $ 5.0",
                                        "image_url" : "https://sethlui.com/wp-content/uploads/2016/01/Hup-Kee-Fried-Oyster-Omelette-630x420.jpg",
                                        "subtitle" : "The oyster omelette is a dish that is widely known for its savoury taste in Taiwan, Fujian and Chaoshan, as well as many parts of Asia",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "oyster omelette"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "More food in the next page!",
                                          "image_url": "https://i5.walmartimages.com/dfw/4ff9c6c9-28f7/k2-_327d5c10-c756-40e0-90cf-d071d67b05a5.v2.jpg",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "View More food",
                                                  "payload": "View More food page 4"
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

def foodpage4(accesstoken, sender):
    ACCESS_TOKEN = accesstoken
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
                                        "title" : "pasta , $ 5.0",
                                        "image_url" : "https://i.ytimg.com/vi/6aVOjLuw-Qg/maxresdefault.jpg",
                                        "subtitle" : "Pasta is a staple food of traditional Italian cuisine, with the first reference dating to 1154 in Sicily. Also commonly used to refer to the variety of pasta dishes, pasta is typically made from an unleavened dough of a durum wheat flour mixed with water ",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "pasta"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "pho , $ 4.0",
                                          "image_url": "https://taxiairport.vn/uploads/ckeditor/images/%5E7773CA1C492E6FA75D868CBFEEEB798876EDFC409543529799%5Epimgpsh_fullsize_distr.png",
                                          "subtitle": "Phở or pho is a Vietnamese soup consisting of broth, rice noodles called bánh phở, a few herbs, and meat, primarily made with either beef or chicken.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "pho"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "pho bo , $ 4.0",
                                        "image_url" : "http://thila.com.vn/en/upload/pho-bo-bap-hoa-30-11-2017-17-52-15.jpg?w=400&h=400&zc=0&q=100&",
                                        "subtitle" : "Phở or pho is a Vietnamese soup consisting of broth, rice noodles called bánh phở, a few herbs, and meat, primarily made with either beef or chicken.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "pho bo"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "rojak , $ 4.0",
                                        "image_url" : "http://www.visitsingapore.com/dining-drinks-singapore/local-dishes/rojak/_jcr_content/par-carousel/carousel_detailpage/carousel/item_2.thumbnail.carousel-img.740.416.jpg",
                                        "subtitle" : "Rojak or Rujak is a traditional fruit and vegetable salad dish commonly found in Indonesia, Malaysia and Singapore. Other than referring to this fruit salad dish, the term rojak also means 'mixture' or 'eclectic mix' in colloquial Malay.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "rojak"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "spaghetti with ham and mushroom , $ 5.0",
                                          "image_url": "https://www.simplyrecipes.com/wp-content/uploads/2006/09/italian-sausage-spaghetti-vertical-a-600.jpg",
                                          "subtitle": "Quick and easy spaghetti recipe with Italian sausage. The tomato-based sauce gets its seasoning from the sweet and spicy sausages. Our favorite way to make spaghetti!",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "spaghetti with ham and mushroom"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "roti prata , $ 1.0",
                                          "image_url": "http://www.visitsingapore.com/content/dam/desktop/global/dining-drinks-singapore/local-dishes/roti-prata-carousel01-square.jpeg",
                                          "subtitle": "Savour the delicious roti prata which is crispy on the outside but soft on the inside. This South-Indian flatbread will always satisfy your palette.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "roti prata"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "satay , $ 0.5",
                                        "image_url" : "https://www.irishtimes.com/polopoly_fs/1.2854640.1478261927!/image/image.jpg_gen/derivatives/landscape_620/image.jpg",
                                        "subtitle" : "Satay, or sate in Indonesian spelling, is a dish of seasoned, skewered and grilled meat, served with a sauce.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "satay"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "spaghetti with chicken chop , $ 5.0",
                                        "image_url" : "http://1.bp.blogspot.com/-VKJwtLwNayI/UIN_P8EUNVI/AAAAAAAACAA/SuES6VlzQEQ/s1600/IMG_9499+edit.JPG",
                                        "subtitle" : "Chicken Chop in mushroom sauce with pasta in tomato sauce and saute assorted capsicum!",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "spaghetti with chicken chop"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "spaghetti with chicken cutlet , $ 5.0",
                                        "image_url" : "https://search.chow.com/thumbnail/800/0/www.chowstatic.com/assets/2015/04/31394_chicken_parmesan_spaghetti_inline_640_2.jpg",
                                        "subtitle" : "Chicken Cutlets and Spaghetti with Peppers and Onions",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "spaghetti with chicken cutlet"
                                              }
                                          ]
                                      },
                                      {
                                          "title": "More food in the next page!",
                                          "image_url": "https://i5.walmartimages.com/dfw/4ff9c6c9-28f7/k2-_327d5c10-c756-40e0-90cf-d071d67b05a5.v2.jpg",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "View More food",
                                                  "payload": "View More food page 5"
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


def drinkspage1(accesstoken, sender):
    ACCESS_TOKEN = accesstoken
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
                                        "title" : "beer gao , $ 5.0",
                                        "image_url" : "https://tottstore.com/wp-content/uploads/2018/08/Beer-Gao.jpg",
                                        "subtitle" : " Beer Gao, is made by adding Guinness Foreign Extra Stout to your beer.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "beer gao"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "coffee , $ 1.0",
                                        "image_url" : "https://www.gardenoflife.com/content/wp-content/uploads/2015/03/organic-coffee-the-choice-to-go-organic-499x392.jpg",
                                        "subtitle" : "Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain Coffea species.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "coffee"
                                              }
                                          ]
                                      },
                                      {

                                        "title" : "iced coffee , $ 1.5",
                                        "image_url" : "https://pioneerwoman.files.wordpress.com/2013/06/iced3.jpg",
                                        "subtitle" : "Iced coffee is a type of coffee served cold, brewed various brewing methods, with the fundamental division being cold brew – brewing the coffee cold, yielding different flavor, but not requiring cooling – or brewing hot and then cooling, generally by simp",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "iced coffee"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "iced milk tea , $ 1.5",
                                        "image_url" : "http://danielfooddiary.com/wp-content/uploads/2015/04/thaimilktea5.jpg",
                                        "subtitle" : "This drink is made with black tea and evaporated milk, or sometimes sweetened condensed milk and was heavily influenced by English customs",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "iced milk tea"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "iced milo , $ 1.5",
                                        "image_url" : "https://cmp.pastamaniadelivery.sg/media/dev_team/products/main-image/52564094ae9f04ecbfa6a4627db106b8.jpg",
                                        "subtitle" : "Milo manufactured in Malaysia is made to dissolve well in hot water to produce a smooth hot chocolate drink, with ice added for a cold drink.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "iced milo"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "kopi , $ 1.0",
                                        "image_url" : "https://d22ir9aoo7cbf6.cloudfront.net/wp-content/uploads/sites/2/2018/04/kopi-singapore-order.jpg",
                                        "subtitle" : "Black coffee with condensed milk and sugar",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "kopi"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "lao hor , $ 5.0",
                                        "image_url" : "https://www.theheinekencompany.com/-/media/Websites/TheHEINEKENCompany/Images/Content/Brands/International-Brands/Tiger/ModA-History.ashx?h=410&w=640&hash=66C923013511387ED6F0CEB4C3BDB998D92823ED",
                                        "subtitle" : "Tiger beer",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "lao hor"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "milk tea , $ 1.5",
                                        "image_url" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbLwwYoVhuv9phtQ9GlGuW8byT4ebbwsVGc3FY--yPTeJ1uf1U",
                                        "subtitle" : "Milk tea is a tea drink made from black tea and milk.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "milk tea"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "milo , $ 1.2",
                                        "image_url" : "https://www.mcdonalds.com.my/storage/foods/September2017/thumb2milo-4f13f10312.jpg",
                                        "subtitle" : "Milo manufactured in Malaysia is made to dissolve well in hot water to produce a smooth hot chocolate drink, with ice added for a cold drink.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "milo"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "More drinks in the next page!",
                                          "image_url": "https://i5.walmartimages.com/dfw/4ff9c6c9-28f7/k2-_327d5c10-c756-40e0-90cf-d071d67b05a5.v2.jpg",
                                        "buttons":[
                                              {
                                                  "type": "postback",
                                                  "title": "View More drinks",
                                                  "payload": "View More drinks page 2"
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

def drinkspage2(accesstoken, sender):
    ACCESS_TOKEN = accesstoken
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
                                          "title": "milo bing , $ 1.5",
                                          "image_url": "https://cmp.pastamaniadelivery.sg/media/dev_team/products/main-image/52564094ae9f04ecbfa6a4627db106b8.jpg",
                                          "subtitle": "Milo manufactured in Malaysia is made to dissolve well in hot water to produce a smooth hot chocolate drink, with ice added for a cold drink.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "milo bing"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "soy bean , $ 1.2",
                                        "image_url" : "https://cimg0.ibsrv.net/cimg/www.fitday.com/693x350_85-1/996/soy-20milk-105996.jpg",
                                        "subtitle" : "Soy milk or soymilk is a plant-based drink produced by soaking and grinding soybeans, boiling the mixture, and filtering out remaining particulates. ",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "soy bean"
                                              }
                                          ]
                                      },
                                      {

                                        "title" : "tea , $ 1.2",
                                        "image_url" : "https://o.aolcdn.com/images/dims?crop=8632%2C4171%2C0%2C0&quality=85&format=jpg&resize=630%2C304&image_uri=http%3A%2F%2Fo.aolcdn.com%2Fhss%2Fstorage%2Fmidas%2Fd384d92d616f92d6a71ca43c8c29e6e%2F206336921%2Fcup-of-tea-on-a-blue-stone-background-copy-space-picture-id619268202&client=a1acac3e1b3290917d92&signature=648e4839de07318faef5c75c5678a0b2b92bd0ad",
                                        "subtitle" : "Tea is an aromatic beverage commonly prepared by pouring hot or boiling water over cured leaves of the Camellia sinensis, an evergreen shrub native to Asia.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "tea"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "teh , $ 1.4",
                                        "image_url" : "http://www.urbandesis.com/wp-content/uploads/2015/07/Teh-Tarik_HR_02-1024x685.jpg",
                                        "subtitle" : "Tea is an aromatic beverage commonly prepared by pouring hot or boiling water over cured leaves of the Camellia sinensis, an evergreen shrub native to Asia.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "teh"
                                              }
                                          ]
                                      },
                                      {

                                          "title": "teh bing , $ 1.5",
                                          "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbLwwYoVhuv9phtQ9GlGuW8byT4ebbwsVGc3FY--yPTeJ1uf1U",
                                          "subtitle": "Milk tea is a tea drink made from black tea and milk.",
                                          "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "teh bing"
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

def sidespage1(accesstoken, sender):
    ACCESS_TOKEN = accesstoken
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
                                        "title" : "fries , $ 2.0",
                                        "image_url" : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBEZquRXYGLd7_rYZLSRuiWopZ5FlJ3ha_3PjNGhdt-SnicqMW",
                                        "subtitle" : "French fries, or just fries; chips, finger chips, or French-fried potatoes are batonnet or allumette-cut deep-fried potatoes",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "fries"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "mash potato , $ 2.5",
                                        "image_url" : "https://www.gimmesomeoven.com/wp-content/uploads/2012/11/hummus-mashed-potatoes-1.jpg",
                                        "subtitle" : "Mashed potato or mashed potatoes, colloquially known as mash, is a dish prepared by mashing boiled, peeled potatoes. Cream, butter and garlic are frequently used in preparation and it is frequently whipped at the end. ",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "mash potato"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "salad , $ 3.0",
                                        "image_url" : "http://images.media-allrecipes.com/userphotos/960x960/4552561.jpg",
                                        "subtitle" : "A salad is a dish consisting of a mixture of small pieces of food, usually vegetables. ",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "salad"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "soup , $ 1.5",
                                        "image_url" : "https://img.taste.com.au/xMLpqAj0/w720-h480-cfill-q80/taste/2016/11/pumpkin-soup-with-a-twist-71237-1.jpeg",
                                        "subtitle" : "Soup is a primarily liquid food, generally served warm or hot, that is made by combining ingredients of meat or vegetables with stock, juice, water, or another liquid. ",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "soup"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "spaghetti , $ 3.0",
                                        "image_url" : "https://hips.hearstapps.com/del.h-cdn.co/assets/17/39/2048x1024/landscape-1506456062-delish-spaghetti-meatballs.jpg?resize=1200:*",
                                        "subtitle" : "Spaghetti is a long, thin, solid, cylindrical pasta",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "spaghetti"
                                              }
                                          ]
                                      },
                                      {
                                        "title" : "toast cube , $ 1.5",
                                        "image_url" : "https://www.recipetineats.com/wp-content/uploads/2015/03/Cinnamon-Sugar-French-Toast-Bites-1.jpg",
                                        "subtitle" : "Cube toast is a dessert dish that consists of brioche cooked as French toast formed in an upright position that is filled with foods such as vanilla ice cream, granola, mochi, Pocky candy, cubed pieces.",
                                        "buttons": [
                                              {
                                                  "type": "postback",
                                                  "title": "Order now",
                                                  "payload": "toast cube"
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