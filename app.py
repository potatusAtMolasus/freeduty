# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app)

age_confirmed = False

@app.route('/ping', methods=['POST'])
def ping_pong():
    return jsonify('pong!')

@app.route('/confirm-age', methods=['POST'])
def check_age():
    # return jsonify(True)
    return jsonify(age_confirmed)

@app.route('/age-confirmed', methods=['POST'])
def confirm_age():
    global age_confirmed
    age_confirmed = True
    return jsonify(True)

@app.route('/find', methods=['POST'])
def find():
    return jsonify([{
        'id': 1,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 3,
        'title': "Текила Монтезума Белая 40% 0,75л",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 4,
        'title': "You may think he loves you for your money 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 5,
        'title': "But I Know What he Actually loves you For 15% 0,6л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",        
        'popularity': "9.1", 
    }, {
        'id': 6,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 7,
        'title': "Thats your brand new Leopard Skin PilBox Hat 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 8,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }])
    
@app.route('/get-categories', methods=['POST'])
def get_categories():
    return jsonify([{
        'url':'/search/1',
        'label': 'Категория 1',
    }, {
        'url':'/search/2',
        'label': 'Категория 2',
    }, {
        'url':'/search/3',
        'label': 'Категория 3',
    }, {
        'url':'/search/4',
        'label': 'Категория 4',
    }, {
        'url':'/search/5',
        'label': 'Категория 5',
    }, {
        'url':'/search/6',
        'label': 'Категория 6',
    }, {
        'url':'/search/7',
        'label': 'Категория 7',
    }, {
        'url':'/search/8',
        'label': 'Категория 8',
    }])

@app.route('/get-offers', methods=['POST'])
def get_offers():

        # 'id': 1,
        # 'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        # 'image': "image.jpg",
        # 'description': "",
        # 'country': "",
        # 'price': "3290",
        # 'salePrice': "2 699.00",
        # 'sale': "2 699.00",
        # 'category': "",
        # 'volume': "",
        # 'strength': "",
        # 'brand': "",
        # 'popularity': "", 
    return jsonify([{
        'id': 1,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 3,
        'title': "Текила Монтезума Белая 40% 0,75л",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 4,
        'title': "You may think he loves you for your money 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 5,
        'title': "But I Know What he Actually loves you For 15% 0,6л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",        
        'popularity': "9.1", 
    }, {
        'id': 6,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 7,
        'title': "Thats your brand new Leopard Skin PilBox Hat 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 8,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }])

@app.route('/get-popular', methods=['POST'])
def get_popular():
    return jsonify([{
        'id': 1,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 3,
        'title': "Текила Монтезума Белая 40% 0,75л",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 4,
        'title': "You may think he loves you for your money 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 5,
        'title': "But I Know What he Actually loves you For 15% 0,6л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1",         
    }, {
        'id': 6,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': False,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 7,
        'title': "Thats your brand new Leopard Skin PilBox Hat 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }, {
        'id': 8,
        'title': "Коньяк Максим Трижоль ВС Эйфелева Башня 40% 0,5л п/у",
        'image': "image.jpg",
        'salePrice': "2 699.00",
        'sale': True,
        'price': "3290",
        'popularity': "9.1", 
    }])

@app.route('/get-posts', methods=['POST'])
def get_posts():
    return jsonify([{
        'id': 1,
        'title': "Фламинго",
        'images': ["flamingo.jpg","man.jpg", "climate.jpg",],
        'text': """white, pink, green or blue
                show off your natural hue
                flamingo, Oh oh o-uuu-o
                if you're multicolored, that's cool too"""
    }, {
        'id': 2,
        'title': "Глобусы",
        'images': ["image.jpg"],
        'text': """Гло гло гло-бу-сы
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, saepe!"""
    }, {
        'id': 3,
        'title': "Глобальное потепление",
        'images': ["climate.jpg"],
        'text': """Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque, saepe!"""
    }, {
        'id': 4,
        'title': "Конь Боджек",
        'images': ["man.jpg", "climate.jpg", "flamingo.jpg"],
        'text': """Back in the 90s I was in a very famous tv show
                Bojack the horse, Bojack the horse don't act like you don't know
                And i'm trying to hold on to my past
                it's been so long i don't think that i am gonna last
                i guess i'll just try and make you understand
                That i'm more a horse than a man
                Or i'm more man than a horse"""
    }, {
        'id': 5,
        'title': "Канье Вест",
        'images': ["ye.png","discount.png"],
        'text': """Grrrat-gat (I can still feel the love)
                Gat-gat-gat-gat-gat
                Grrrat-gat-gat-gat (I can still feel the love)
                Grrrat-gat-gat-gat-gat-gat (feel the love)
                Grrrat
                Ba-ba-ba-ba
                Brrat-tat-da-da-da-da
                Ga-ga-ga-ga
                Brrr-ah-da-da, brrr-ah-da-da
                Brrr-ah-da-da-da, brrr-ah-da-da-da
                Brrr-ah-brrr-ah, brrr-ah-ga-grrrat
                Ru-ru-ru-ru-oh!"""
    }, {
        'id': 6,
        'title': "Работа Фронтэндера",
        'images': ["discount.png"],
        'text': "Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque in sequi illo laborum neque."
    }])

@app.route('/get-filters', methods=['POST'])
def get_filters():   
    return jsonify({
        'categories': [
            {'value': 'vino', 'label': 'Вино'},
            {'value': 'vodka', 'label': 'Вока'},
            {'value': 'konjak', 'label': 'Коньяк'},
            {'value': 'viski', 'label': 'Виски'}
        ],
        'brands': [
            {'value': 'fanagoria', 'label': 'Fanagoria'},
            {'value': 'sangria', 'label': 'Sangria'},
            {'value': 'bells', 'label': 'Bells'},
            {'value': 'jack', 'label': 'Jack'}
        ],
        'countries': [
            {'value': 'russia', 'label': 'Россия'},
            {'value': 'england', 'label': 'Великобритания'},
            {'value': 'usa', 'label': 'США'},
            {'value': 'ukraine', 'label': 'Украина'}
        ],
    })

if __name__ == '__main__':
    app.run()