CREATE DATABASE  IF NOT EXISTS `heroku_b719ec770e665f0` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `heroku_b719ec770e665f0`;
-- MySQL dump 10.13  Distrib 5.7.23, for Win64 (x86_64)
--
-- Host: us-cdbr-iron-east-01.cleardb.net    Database: heroku_b719ec770e665f0
-- ------------------------------------------------------
-- Server version	5.5.56-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `drinks`
--

DROP TABLE IF EXISTS `drinks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `drinks` (
  `dname` varchar(255) NOT NULL,
  `dprice` float NOT NULL,
  `ddescription` varchar(255) DEFAULT NULL,
  `dpic` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`dname`),
  UNIQUE KEY `dname_UNIQUE` (`dname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drinks`
--

LOCK TABLES `drinks` WRITE;
/*!40000 ALTER TABLE `drinks` DISABLE KEYS */;
INSERT INTO `drinks` VALUES ('beer gao',5,' Beer Gao, is made by adding Guinness Foreign Extra Stout to your beer.','https://tottstore.com/wp-content/uploads/2018/08/Beer-Gao.jpg'),('coffee',1,'Coffee is a brewed drink prepared from roasted coffee beans, the seeds of berries from certain Coffea species.','https://www.gardenoflife.com/content/wp-content/uploads/2015/03/organic-coffee-the-choice-to-go-organic-499x392.jpg'),('iced coffee',1.5,'Iced coffee is a type of coffee served cold, brewed various brewing methods, with the fundamental division being cold brew – brewing the coffee cold, yielding different flavor, but not requiring cooling – or brewing hot and then cooling, generally by simp','https://pioneerwoman.files.wordpress.com/2013/06/iced3.jpg'),('iced milk tea',1.5,'This drink is made with black tea and evaporated milk, or sometimes sweetened condensed milk and was heavily influenced by English customs','http://danielfooddiary.com/wp-content/uploads/2015/04/thaimilktea5.jpg'),('iced milo',1.5,'Milo manufactured in Malaysia is made to dissolve well in hot water to produce a smooth hot chocolate drink, with ice added for a cold drink.','https://cmp.pastamaniadelivery.sg/media/dev_team/products/main-image/52564094ae9f04ecbfa6a4627db106b8.jpg'),('kopi',1,'Black coffee with condensed milk and sugar','https://d22ir9aoo7cbf6.cloudfront.net/wp-content/uploads/sites/2/2018/04/kopi-singapore-order.jpg'),('lao hor',5,'Tiger beer','https://www.theheinekencompany.com/-/media/Websites/TheHEINEKENCompany/Images/Content/Brands/International-Brands/Tiger/ModA-History.ashx?h=410&w=640&hash=66C923013511387ED6F0CEB4C3BDB998D92823ED'),('milk tea',1.5,'Milk tea is a tea drink made from black tea and milk.','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbLwwYoVhuv9phtQ9GlGuW8byT4ebbwsVGc3FY--yPTeJ1uf1U'),('milo',1.2,'Milo manufactured in Malaysia is made to dissolve well in hot water to produce a smooth hot chocolate drink, with ice added for a cold drink.','https://www.mcdonalds.com.my/storage/foods/September2017/thumb2milo-4f13f10312.jpg'),('milo bing',1.5,'Milo manufactured in Malaysia is made to dissolve well in hot water to produce a smooth hot chocolate drink, with ice added for a cold drink.','https://cmp.pastamaniadelivery.sg/media/dev_team/products/main-image/52564094ae9f04ecbfa6a4627db106b8.jpg'),('soy bean',1.2,'Soy milk or soymilk is a plant-based drink produced by soaking and grinding soybeans, boiling the mixture, and filtering out remaining particulates. ','https://cimg0.ibsrv.net/cimg/www.fitday.com/693x350_85-1/996/soy-20milk-105996.jpg'),('tea',1.2,'Tea is an aromatic beverage commonly prepared by pouring hot or boiling water over cured leaves of the Camellia sinensis, an evergreen shrub native to Asia.','https://cbtl-images.s3.us-west-1.amazonaws.com/Production/Drupal/s3fs-public/styles/cafe_menu_item_teaser/public/cafe-menu/Hot-Black-Tea.jpg?itok=dYziJ_Tq'),('teh',1.4,'Tea is an aromatic beverage commonly prepared by pouring hot or boiling water over cured leaves of the Camellia sinensis, an evergreen shrub native to Asia.','https://cbtl-images.s3.us-west-1.amazonaws.com/Production/Drupal/s3fs-public/styles/cafe_menu_item_teaser/public/cafe-menu/Hot-Black-Tea.jpg?itok=dYziJ_Tq'),('teh bing',1.5,'Milk tea is a tea drink made from black tea and milk.','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQbLwwYoVhuv9phtQ9GlGuW8byT4ebbwsVGc3FY--yPTeJ1uf1U');
/*!40000 ALTER TABLE `drinks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food` (
  `fname` varchar(255) NOT NULL,
  `fprice` float NOT NULL,
  `fdescription` varchar(255) DEFAULT NULL,
  `fpic` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`fname`),
  UNIQUE KEY `fname` (`fname`),
  UNIQUE KEY `fname_UNIQUE` (`fname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
INSERT INTO `food` VALUES ('aglio olio chicken chop',5,'This dish is made by lightly sauteeing sliced, minced, or pressed garlic in olive oil, sometimes with the addition of dried red chili flakes, and tossing with spaghetti topped with chicken chop','http://4.bp.blogspot.com/-7UwaNrcWZqI/TrFHDzzFHzI/AAAAAAAAKd0/UtaHvJhV0QE/s1600/Grilled+Chicken+with+Pasta+Aglio+E+Olio+October+31st%252C+2011.jpg'),('aglio olio chicken cutlet',5,'This dish is made by lightly sauteeing sliced, minced, or pressed garlic in olive oil, sometimes with the addition of dried red chili flakes, and tossing with spaghetti topped with chicken cutlet.','http://cookdiary.net/wp-content/uploads/images/Chicken-and-Noodles.jpg'),('bak chor mee',4,'Bak Chor Mee (肉脞面) literally means “minced meat and noodles” in the Teochew dialect.','https://mtc1-dydfxmh.netdna-ssl.com/wp-content/uploads/2017/03/P1040774-1300x867.jpg'),('bak kut teh',5,'Singapore Teochew Bak Kut Teh is a version of pork ribs tea with a clear garlicky and peppery broth. Only a few ingredients and very easy to prepare.','https://www.rotinrice.com/wp-content/uploads/2016/12/ST-BakKutTeh-1.jpg'),('bee hoon',1.2,'Rice vermicelli are a thin form of rice noodles. They are sometimes referred to as rice noodles, rice sticks, or bee hoon, but they should not be confused with cellophane noodles which are a different Asian type of vermicelli made from mung bean starch or','https://s3-ap-southeast-1.amazonaws.com/afc-prod/thumbnails/standard_mobile/5415/0286/1193/tn-HFM-Braised-Pig-Trotter-Bee-Hoon.jpg'),('beef',4,'Beef is the culinary name for meat from cattle, particularly skeletal muscle.','http://irepo.primecp.com/2016/02/253740/Dads-Beer-Marinated-Steak_ExtraLarge1000_ID-1395178.jpg?v=1395178'),('biryani',4,'Biryani, also known as biriyani, biriani, birani or briyani, \'spicy rice\' is a South Asian mixed rice dish with its origins among the Muslims of the Indian subcontinent.','http://www.ndtv.com/cooks/images/mutton-biryani-new.jpg'),('bun bo hue',5,'Bún bò Huế or bún bò is a popular Vietnamese soup containing rice vermicelli (bún) and beef (bò). Huế is a city in central Vietnam associated with the cooking style of the former royal court. The dish is greatly admired for its balance of spicy, sour, sal','https://media.foody.vn/res/g65/642530/prof/s/foody-mobile-ba-thu-jpg-537-636255976625248994.jpg'),('char kway teow',3,'Char kway teow, literally \'stir-fried ricecake strips\', is a popular noodle dish in Malaysia, Singapore, Brunei and Indonesia. The dish is considered a national favourite in Malaysia and Singapore','https://www.nyonyacooking.com/images/recipes/char-kway-teow.jpg'),('chicken burger',3,'A hot sandwich made of a patty of chicken in a bun, often with other ingredients.','https://www.chicken.ca/assets/RecipePhotos/_resampled/FillWyI3MjAiLCI2MDAiXQ/Moist-Chicken-Burgers.jpg'),('chicken rice',3,'Hainanese chicken rice is a dish adapted from early Chinese immigrants originally from Hainan province in southern China.','https://upload.wikimedia.org/wikipedia/commons/7/71/Hainanese_Chicken_Rice.jpg'),('crabs',20,'Chilli crab is a popular seafood dish among locals and foreigners in Singapore, and consists of mud crabs deep-fried in a sweet, savoury and spicy gravy.','https://www.thespruceeats.com/thmb/iR3fKo4lRqANDPkfUsmPaTl7qxg=/4738x2533/filters:no_upscale():max_bytes(150000):strip_icc()/close-up-of-crab-gravy-served-on-table-677147575-588b52995f9b5874ee1af765.jpg'),('curry fish head',18,'Fish head curry is a dish in Singaporean and Malaysian cuisine with Indian and Chinese origins. The head of a red snapper is semi-stewed in a Kerala-style curry with assorted vegetables such as okra and eggplants.','https://farm5.staticflickr.com/4233/35800092885_902a64e85b_o.jpg'),('dim sum',1.2,'Dim sum is a style of Chinese cuisine prepared as small bite-sized portions of food served in small steamer baskets or on small plates. Dim sum dishes are usually served with tea and together form a full tea brunch. Dim sum traditionally are served as ful','https://dynaimage.cdn.cnn.com/cnn/q_auto,w_900,c_fill,g_auto,h_506,ar_16:9/http%3A%2F%2Fcdn.cnn.com%2Fcnnnext%2Fdam%2Fassets%2F160325033254-hk-dim-sum-fook-lam-moon.jpg'),('fish burger',3,'A hot sandwich made of a fish fillet in a bun, often with other ingredients.','https://d1yupijb0jmhpf.cloudfront.net/52929f79-a794-4249-8a8f-bafe64b35a4a.png'),('fish n chips',5,'Fish and chips is a hot dish of English origin consisting of fried battered fish and hot potato chips. It is a common take-away food and an early example of culinary fusion.','https://d2iq9gqtfwsete.cloudfront.net/wp-content/uploads/2017/11/mcd3.jpg?x20326'),('fried carrot cake',3,'Fried carrot cake, or chai tow kway in the Teochew dialect, consists of cubes of radish cake stir-fried with garlic, eggs and preserved radish.','http://www.singaporebestfoods.com/wp-content/uploads/2017/09/Yuan-Cheng-Fried-Carrot-Cake-3.jpg'),('fried hokkien mee',5,'Hokkien mee is a dish in Malaysian and Singaporean cuisine that has its origins in the cuisine of China\'s Fujian province.','https://mtc1-dydfxmh.netdna-ssl.com/wp-content/uploads/2016/12/16069838051_c75eb4dd99_o-1300x867.jpg'),('hokkien char mee',4,'福建炒麵) is served in Kuala Lumpur and the surrounding region. It is a dish of thick yellow noodles braised in thick dark soy sauce with pork, squid, fish cake and cabbage as the main ingredients and cubes of pork fat fried until crispy (sometimes pork liver','http://p1.meituan.net/poirichness/menu_6597338_58965842.jpg%40249w_249h_1e_1c_1l%7Cwatermark%3D1%26%26r%3D1%26p%3D9%26x%3D2%26y%3D2%26relative%3D1%26o%3D20'),('hokkien prawn mee',4,'Hokkien Prawn Mee, also affectionately known as 福建蝦麵, is another favourite of every local in Singapore.','https://rasamalaysia.com/wp-content/uploads/2011/01/hokkien-mee-8.jpg'),('laksa',4,'Laksa consists of rice noodles or rice vermicelli with chicken, prawn or fish, served in spicy soup based on either rich and spicy curry coconut milk or on sour asam.','https://makanzeit.files.wordpress.com/2018/02/sungei_road_laksa_resize.png'),('mee siam',4,'Mee siam, which means \'Siamese noodle\' in Malay, is a dish of thin rice vermicelli popular in Singapore and Malaysia.','http://mayakitchenette.com/wp-content/uploads/2014/07/mee-siam-recipe-3.jpg'),('nasi lemak',3,'Nasi lemak is a Malay fragrant rice dish cooked in coconut milk and pandan leaf. It is commonly found in Malaysia, where it is considered the national dish; it is also popular in neighbouring areas such as Singapore; Brunei, and Southern Thailand.','https://d1alt1wkdk73qo.cloudfront.net/images/guide/6abb55670f06cebacdc5023d11367153/640x478_ac.jpg'),('noodle',2,'A very thin, long strip of pasta or a similar flour paste, eaten with a sauce or in a soup.','https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Mama_instant_noodle_block.jpg/1200px-Mama_instant_noodle_block.jpg'),('oyster omelette',5,'The oyster omelette is a dish that is widely known for its savoury taste in Taiwan, Fujian and Chaoshan, as well as many parts of Asia','https://sethlui.com/wp-content/uploads/2016/01/Hup-Kee-Fried-Oyster-Omelette-630x420.jpg'),('pasta',5,'Pasta is a staple food of traditional Italian cuisine, with the first reference dating to 1154 in Sicily. Also commonly used to refer to the variety of pasta dishes, pasta is typically made from an unleavened dough of a durum wheat flour mixed with water ','https://i.ytimg.com/vi/6aVOjLuw-Qg/maxresdefault.jpg'),('pho',4,'Phở or pho is a Vietnamese soup consisting of broth, rice noodles called bánh phở, a few herbs, and meat, primarily made with either beef or chicken.','https://taxiairport.vn/uploads/ckeditor/images/%5E7773CA1C492E6FA75D868CBFEEEB798876EDFC409543529799%5Epimgpsh_fullsize_distr.png'),('pho bo',4,'Phở or pho is a Vietnamese soup consisting of broth, rice noodles called bánh phở, a few herbs, and meat, primarily made with either beef or chicken.','http://thila.com.vn/en/upload/pho-bo-bap-hoa-30-11-2017-17-52-15.jpg?w=400&h=400&zc=0&q=100&'),('rojak',4,'Rojak or Rujak is a traditional fruit and vegetable salad dish commonly found in Indonesia, Malaysia and Singapore. Other than referring to this fruit salad dish, the term rojak also means \'mixture\' or \'eclectic mix\' in colloquial Malay.','http://www.visitsingapore.com/dining-drinks-singapore/local-dishes/rojak/_jcr_content/par-carousel/carousel_detailpage/carousel/item_2.thumbnail.carousel-img.740.416.jpg'),('roti prata',1,'Savour the delicious roti prata which is crispy on the outside but soft on the inside. This South-Indian flatbread will always satisfy your palette.','http://www.visitsingapore.com/content/dam/desktop/global/dining-drinks-singapore/local-dishes/roti-prata-carousel01-square.jpeg'),('satay',3,'Satay, or sate in Indonesian spelling, is a dish of seasoned, skewered and grilled meat, served with a sauce.','https://www.irishtimes.com/polopoly_fs/1.2854640.1478261927!/image/image.jpg_gen/derivatives/landscape_620/image.jpg'),('spaghetti with chicken chop',5,'Chicken Chop in mushroom sauce with pasta in tomato sauce and saute assorted capsicum!','http://1.bp.blogspot.com/-VKJwtLwNayI/UIN_P8EUNVI/AAAAAAAACAA/SuES6VlzQEQ/s1600/IMG_9499+edit.JPG'),('spaghetti with chicken cutlet',5,'Chicken Cutlets and Spaghetti with Peppers and Onions','https://search.chow.com/thumbnail/800/0/www.chowstatic.com/assets/2015/04/31394_chicken_parmesan_spaghetti_inline_640_2.jpg'),('spaghetti with ham and mushroom',5,'Quick and easy spaghetti recipe with Italian sausage. The tomato-based sauce gets its seasoning from the sweet and spicy sausages. Our favorite way to make spaghetti!','https://www.simplyrecipes.com/wp-content/uploads/2006/09/italian-sausage-spaghetti-vertical-a-600.jpg'),('spaghetti with sausage',5,'Delicious pieces of ham add a meaty touch to this hearty pasta dish.','https://img.taste.com.au/pSKAAN57/w720-h480-cfill-q80/taste/2016/11/mushroom-and-ham-spaghetti-25701-1.jpeg'),('wanton mee',3,'Wonton noodles is a Cantonese noodle dish which is popular in Guangzhou, Hong Kong, Malaysia, Singapore and Thailand.','https://c4.staticflickr.com/8/7386/27790732171_558d9ac9d3_b.jpg');
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sides`
--

DROP TABLE IF EXISTS `sides`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sides` (
  `sname` varchar(255) NOT NULL,
  `sprice` float NOT NULL,
  `sdescription` varchar(255) DEFAULT NULL,
  `spic` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`sname`),
  UNIQUE KEY `sname` (`sname`),
  UNIQUE KEY `sname_UNIQUE` (`sname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sides`
--

LOCK TABLES `sides` WRITE;
/*!40000 ALTER TABLE `sides` DISABLE KEYS */;
INSERT INTO `sides` VALUES ('fries',2,'French fries, or just fries; chips, finger chips, or French-fried potatoes are batonnet or allumette-cut deep-fried potatoes','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBEZquRXYGLd7_rYZLSRuiWopZ5FlJ3ha_3PjNGhdt-SnicqMW'),('mash potato',2.5,'Mashed potato or mashed potatoes, colloquially known as mash, is a dish prepared by mashing boiled, peeled potatoes. Cream, butter and garlic are frequently used in preparation and it is frequently whipped at the end. ','https://www.gimmesomeoven.com/wp-content/uploads/2012/11/hummus-mashed-potatoes-1.jpg'),('salad',3,'A salad is a dish consisting of a mixture of small pieces of food, usually vegetables. ','http://images.media-allrecipes.com/userphotos/960x960/4552561.jpg'),('soup',1.5,'Soup is a primarily liquid food, generally served warm or hot, that is made by combining ingredients of meat or vegetables with stock, juice, water, or another liquid. ','https://img.taste.com.au/xMLpqAj0/w720-h480-cfill-q80/taste/2016/11/pumpkin-soup-with-a-twist-71237-1.jpeg'),('spaghetti',3,'Spaghetti is a long, thin, solid, cylindrical pasta','https://hips.hearstapps.com/del.h-cdn.co/assets/17/39/2048x1024/landscape-1506456062-delish-spaghetti-meatballs.jpg?resize=1200:*'),('toast cube',1.8,'Cube toast is a dessert dish that consists of brioche cooked as French toast formed in an upright position that is filled with foods such as vanilla ice cream, granola, mochi, Pocky candy, cubed pieces.','https://www.recipetineats.com/wp-content/uploads/2015/03/Cinnamon-Sugar-French-Toast-Bites-1.jpg');
/*!40000 ALTER TABLE `sides` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'heroku_b719ec770e665f0'
--

--
-- Dumping routines for database 'heroku_b719ec770e665f0'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-08 23:13:49
