chinesefood = ("char kway teow", "biryani", "oyster omelette", "chicken rice", "pasta", "satay", "hokkien prawn mee", "fried carrot cake",
               "hokkien char mee", "curry fish head", "noodle", "spaghetti with sausage", "beef", "rojak", "aglio olio chicken cutlet",
               "roti prata", "spaghetti with chicken chop", "aglio olio chicken chop", "bee hoon", "spaghetti with chicken cutlet",
               "bun bo hue", "spaghetti with ham and mushroom", "pho", "mee siam", "dim sum", "wanton mee", "pho bo", "laksa", "chicken burger",
               "bak chor mee", "crabs", "nasi lemak", "fish burger", "bak kut teh", "fried hokkien mee", "fish n chips")

drinks = ("milk tea", "lao hor", "soy bean", "coffee", "kopi", "beer gao")
sides = ("fries", "mash potato", "toast cube", "salad", "soup", "spaghetti")
numbers = open("C:/Users/Asus-Laptop/Desktop/numbers.txt", "r")
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
    for i in chinesefood:
        x = i
        TRAIN_DATA = (
            ("1 large " + x + " please", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'SIZE'),
                             (8, 8+len(x), 'FOOD')]
            }),

            ("2 satay 4 large biryani 5 large chicken rice", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 7, 'FOOD'),
                             (8, 9, 'QUANTITY'),
                             (10, 15, 'SIZE'),
                             (16, 23, 'FOOD'),
                             (24, 25, 'QUANTITY'),
                             (26, 31, 'SIZE'),
                             (32, 44, 'FOOD')]
            }),

            (x + " is a cuisine", {
                'entities': [(0, len(x), 'FOOD')]
            }),

            ("1 " + x + " 3 soup 4 biryani 5 kopi", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, 2+len(x), 'FOOD'),
                             ( len(x) + 3,  len(x) + 4, 'QUANTITY'),
                             ( len(x) + 5,  len(x) + 9, 'SIDES'),
                             ( len(x) + 10,  len(x) + 11, 'QUANTITY'),
                             ( len(x) + 12,  len(x) + 19, 'FOOD'),
                             ( len(x) + 20,  len(x) + 21, 'QUANTITY'),
                             ( len(x) + 22,  len(x) + 26, 'DRINKS')]
            }),

            ("2 " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2,  2 + len(x), 'FOOD')]
            }),

            ("3 medium " + x + " 5 small chicken rice", {
                'entities': [(0, 1, 'QUANTITY'),
                             ( 2,  8, 'SIZE'),
                             ( 9, ( 9 + len(x)), 'FOOD'),
                             ( len(x) + 11,  len(x) + 12, 'QUANTITY'),
                             (( 9 + len(x)) + 4, ( 9 + len(x)) + 9, 'SIZE'),
                             (( 9 + len(x)) + 10, ( 9 + len(x)) + 22, 'FOOD')]
            }),

            ("4 large " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             ( 2,  7, 'SIZE'),
                             ( 8,  8 + len(x), 'FOOD')]
            }),
        )
        for y in TRAIN_DATA:
            trained_data.append(y)


def drinksdatatraining():
    for i in drinks:
        x = i
        TRAIN_DATA = (
            ("2 medium " + x + " please", {
                'entities': [(0, 1, 'QUANTITY'),
                             ( 2,  8, 'SIZE'),
                             ( 9,  9 + len(x), 'DRINKS')]
            }),

            ("1 small milk tea 3 large coffee 5 medium soy bean", {
                'entities': [(0, 1, 'QUANTITY'),
                             ( 2, 7, 'SIZE'),
                             ( 8,  16, 'DRINKS'),
                             (17, 18, 'QUANTITY'),
                             (19,  24, 'SIZE'),
                             ( 25,  31, 'DRINKS'),
                             ( 32,  33, 'QUANTITY'),
                             ( 34,  40, 'SIZE'),
                             ( 41,  49, 'DRINKS')]
            }),

            ("one " + x + " 6 large spaghetti chicken chop", {
                'entities': [(0, 3, 'QUANTITY'),
                             (4,  4 + len(x), 'DRINKS'),
                             (4+len(x)+1, len(x)+6, 'QUANTITY'),
                             (4+len(x)+3, 4+len(x)+8, 'SIZE'),
                             (4+len(x)+9, 4+len(x)+31, 'FOOD')]
            }),

            (x + " taste good", {
                'entities': [(0, len(x), 'DRINKS')]
            }),

             ("1 " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2,  2 + len(x), 'DRINKS')]
            }),

            ("3 " + x + "  3 beer gao", {
                'entities': [(0, 1, 'QUANTITY'),
                             (2, ( 2 + len(x)), 'DRINKS'),
                             ( len(x) + 3,  len(x) + 3 + 1, 'QUANTITY'),
                             ( len(x) + 4 + 1,  len(x) + 12 + 1, 'DRINKS')]
            }),

             ("3 large " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             ( 2,  7, 'SIZE'),
                             ( 8,  8 + len(x), 'DRINKS')]
            }),
        )
        for y in TRAIN_DATA:
                trained_data.append(y)


def sidesdatatraining():
    for i in sides:
        x = i
        TRAIN_DATA = (
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
                             ( 2,  7, 'SIZE'),
                             ( 8,  8 + len(x), 'SIDES')]
            }),

            (x + " taste good", {
                'entities': [(0, len(x), 'SIDES')]
            }),

             ("3 " + x, {
                'entities': [(0, 1, 'QUANTITY'),
                             (2,  2 + len(x), 'SIDES')]
            }),

            ("3 " + x + " 5 toast cube 9 lao hor", {
                'entities': [(0, 1, 'QUANTITY'),
                             ( 2,  2 + len(x), 'SIDES'),
                             ( 3 + len(x),  4 + len(x), 'QUANTITY'),
                             ( 5 + len(x),  15 + len(x), 'SIDES'),
                             ( 16 + len(x),  17 + len(x), 'QUANTITY'),
                             ( 18 + len(x),  25 + len(x), 'DRINKS')]
            }),

            ("2 " + x + " 7 toast cube", {
                'entities': [(0, 1, 'QUANTITY'),
                             ( 2, ( 2 + len(x)), 'SIDES'),
                             ( len(x) + 3,  len(x) + 3 + 1, 'QUANTITY'),
                             ( len(x) + 4 + 1,  len(x) + 14 + 1, 'SIDES')]
            }),
        )
        for y in TRAIN_DATA:
                trained_data.append(y)

# foodtraining()
# print (trained_data)
# print(len(trained_data))

