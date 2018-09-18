food = ("char kway teow", "biryani", "oyster omelette", "chicken rice", "pasta", "satay", "hokkien prawn mee", "fried carrot cake",
               "hokkien char mee", "curry fish head", "noodle", "spaghetti with sausage", "beef", "rojak", "aglio olio chicken cutlet",
               "roti prata", "spaghetti with chicken chop", "aglio olio chicken chop", "bee hoon", "spaghetti with chicken cutlet",
               "bun bo hue", "spaghetti with ham and mushroom", "pho", "mee siam", "dim sum", "wanton mee", "pho bo", "laksa", "chicken burger",
               "bak chor mee", "crabs", "nasi lemak", "fish burger", "bak kut teh", "fried hokkien mee", "fish n chips")

drinks = ("milk tea", "lao hor", "soy bean", "coffee", "kopi", "beer gao", "milo", "tea", "teh", "teh bing", "milo bing",
          "iced milo", "iced coffee", "iced milk tea")

sides = ("fries", "mash potato", "toast cube", "salad", "soup", "spaghetti")

numbers = open("/app/numbers without word forms.txt", "r")
numbers = numbers.read()

trained_data = []


def foodtraining():
    fooddatatraining()
    drinksdatatraining()
    sidesdatatraining()
    numbertraining()
    return trained_data

def numbertraining():
    for i in numbers:
        x = i
        TRAIN_DATA = (
            (x, {
                'entities': [(0, len(x), 'QUANTITY')]
            }),)
        for y in TRAIN_DATA:
            trained_data.append(y)


def fooddatatraining():
    for i in food:
        x = i
        TRAIN_DATA = (

            (x + " is a cuisine", {
                'entities': [(0, len(x), 'FOOD')]
            }),

            ("2 " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2 + len(x), 'FOOD')]
            }),

            ("4 large " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8 + len(x), 'FOOD')]
            }),

            ("3 " + x + " 3 bak kut teh", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2 + len(x), 'FOOD'),
                             (len(x) + 3, len(x) + 4, 'QUANTITY'),
                             (len(x) + 5, len(x) + 16, 'FOOD')]
            }),

            ("3 medium " + x + " 5 small chicken rice", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 8, 'SIZE'),
                             (9, 9 + len(x), 'FOOD'),
                             (len(x) + 10, len(x) + 11, 'QUANTITY'),
                             (len(x) + 12, len(x) + 17, 'SIZE'),
                             (len(x) + 18, len(x) + 30, 'FOOD')]
            }),

            ("2 small " + x + " 4 large biryani 5 large chicken rice", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8 + len(x), 'FOOD'),
                             (9 + len(x), 10 + len(x), 'QUANTITY'),
                             (11 + len(x), 16 + len(x), 'SIZE'),
                             (17 + len(x), 24 + len(x), 'FOOD'),
                             (25 + len(x), 26 + len(x), 'QUANTITY'),
                             (27 + len(x), 31 + len(x), 'SIZE'),
                             (32 + len(x), 44 + len(x), 'FOOD')]
            }),



            ("1 " + x + " 3 soup 4 biryani 5 kopi", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2+len(x), 'FOOD'),
                             (len(x) + 3,  len(x) + 4, 'QUANTITY'),
                             (len(x) + 5,  len(x) + 9, 'SIDES'),
                             (len(x) + 10,  len(x) + 11, 'QUANTITY'),
                             (len(x) + 12,  len(x) + 19, 'FOOD'),
                             (len(x) + 20,  len(x) + 21, 'QUANTITY'),
                             (len(x) + 22,  len(x) + 26, 'DRINKS')]
            }),

            ("2 small " + x + " 4 large coffee 5 medium fries", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8+len(x), 'FOOD'),
                             (9+len(x), 10+len(x), 'QUANTITY'),
                             (11+len(x), 16+len(x), 'SIZE'),
                             (17+len(x), 23+len(x), 'DRINKS'),
                             (24+len(x), 25+len(x), 'QUANTITY'),
                             (26+len(x), 32+len(x), 'SIZE'),
                             (33+len(x), 38+len(x), 'SIDES')]
            }),
        )
        for y in TRAIN_DATA:
            trained_data.append(y)


def drinksdatatraining():
    for i in drinks:
        x = i
        TRAIN_DATA = (

            (x + " taste good", {
                'entities': [(0, len(x), 'DRINKS')]
            }),

            ("1 " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2 + len(x), 'DRINKS')]
            }),

            ("2 medium " + x + " please", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2,  8, 'SIZE'),
                             (9,  9 + len(x), 'DRINKS')]
            }),

            ("1 small " + x + " 6 large spaghetti chicken chop", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8 + len(x), 'DRINKS'),
                             (9 + len(x), 10 + len(x), 'QUANTITY'),
                             (11 + len(x), 16 + len(x), 'SIZE'),
                             (17 + len(x), 39 + len(x), 'FOOD')]
            }),

            ("1 small " + x + " 3 large coffee 5 medium soy bean", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8,  8 + len(x), 'DRINKS'),
                             (9 + len(x), 10 + len(x), 'QUANTITY'),
                             (11 + len(x),  16 + len(x), 'SIZE'),
                             (17 + len(x),  23 + len(x), 'DRINKS'),
                             (24 + len(x),  25 + len(x), 'QUANTITY'),
                             (26 + len(x),  32 + len(x), 'SIZE'),
                             (33 + len(x),  41 + len(x), 'DRINKS')]
            }),

            ("3 medium " + x + " 5 small milo", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 8, 'SIZE'),
                             (9, 9 + len(x), 'DRINKS'),
                             (len(x) + 10, len(x) + 11, 'QUANTITY'),
                             (len(x) + 12, len(x) + 17, 'SIZE'),
                             (len(x) + 18, len(x) + 22, 'DRINKS')]
            }),

            ("3 " + x + "  3 beer gao", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2 + len(x), 'DRINKS'),
                             (len(x) + 3,  len(x) + 4, 'QUANTITY'),
                             (len(x) + 5,  len(x) + 13, 'DRINKS')]
            }),

            ("4 small " + x + " 5 small mash potato 2 medium nasi lemak ", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8,  8 + len(x), 'DRINKS'),
                             (9 + len(x),  10 + len(x), 'QUANTITY'),
                             (11 + len(x), 16 + len(x), 'SIZE'),
                             (17 + len(x), 28 + len(x), 'SIDES'),
                             (29 + len(x), 30 + len(x), 'QUANTITY'),
                             (31 + len(x), 37 + len(x), 'SIZE'),
                             (38 + len(x), 48 + len(x), 'FOOD')]
            }),
        )
        for y in TRAIN_DATA:
                trained_data.append(y)


def sidesdatatraining():
    for i in sides:
        x = i
        TRAIN_DATA = (

            (x + " taste good", {
                'entities': [(0, len(x), 'SIDES')]
            }),

            ("3 " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2 + len(x), 'SIDES')]
            }),

            ("1 small " + x + " please", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8+len(x), 'SIDES')]
            }),

            ("two large spaghetti 4 small fries 5 large mash potato", {
                'entities': [(0, 3, 'QUANTITY'),
                             ( 4,  9, 'SIZE'),
                             (10, 19, 'SIDES'),
                             ( 20,  21, 'QUANTITY'),
                             (22, 27, 'SIZE'),
                             (28, 33, 'SIDES'),
                             ( 34,  35, 'QUANTITY'),
                             (35, 41, 'SIZE'),
                             (41, 53, 'SIDES')]
            }),

             ("2 large " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2,  7, 'SIZE'),
                             (8,  8 + len(x), 'SIDES')]
            }),

            ("8 " + x + "  9 salad", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2 + len(x), 'SIDES'),
                             (len(x) + 3, len(x) + 4, 'QUANTITY'),
                             (len(x) + 5, len(x) + 10, 'SIDES')]
            }),

            ("3 small " + x + " 5 medium toast cube 9 large lao hor", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8,  8 + len(x), 'SIDES'),
                             (9 + len(x),  10 + len(x), 'QUANTITY'),
                             (11 + len(x), 12 + len(x), 'SIZE'),
                             (13 + len(x),  23 + len(x), 'SIDES'),
                             (24 + len(x),  25 + len(x), 'QUANTITY'),
                             (26 + len(x), 27 + len(x), 'SIZE'),
                             (28 + len(x),  35 + len(x), 'DRINKS')]
            }),

            ("2 large " + x + " 7 large toast cube", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8 + len(x), 'SIDES'),
                             (len(x) + 9,  len(x) + 10, 'QUANTITY'),
                             (len(x) + 11, len(x) + 16, 'SIZE'),
                             (len(x) + 17,  len(x) + 27, 'SIDES')]
            }),

            ("5 large " + x + " 2 large bak chor mee 4 medium kopi", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8 + len(x), 'SIDES'),
                             (9 + len(x), 10 + len(x), 'QUANTITY'),
                             (11 + len(x), 16 + len(x), 'SIZE'),
                             (17 + len(x), 29 + len(x), 'FOOD'),
                             (30 + len(x), 31 + len(x), 'QUANTITY'),
                             (32 + len(x), 38 + len(x), 'SIZE'),
                             (39 + len(x), 43 + len(x), 'DRINKS')]
            }),
        )
        for y in TRAIN_DATA:
                trained_data.append(y)

# foodtraining()
# print (trained_data)
# print(len(trained_data))

